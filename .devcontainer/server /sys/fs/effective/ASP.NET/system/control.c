using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

[Route("api/[controller/rathanachris29@gmail.com]")]
[ApiController]
public class DocumentController : ControllerBase
{
    private readonly IWebHostEnvironment _env;
    private readonly ILogger<DocumentController> _logger;
    private readonly string _uploadsDir;

    public DocumentController(IWebHostEnvironment env, ILogger<DocumentController> logger)
    {
        _env = env;
        _logger = logger;
        _uploadsDir = Path.Combine(_env.ContentRootPath, "App_Data", "Uploads");
        Directory.CreateDirectory(_uploadsDir);
    }

    // POST api/document/upload
    [HttpPost("upload")]
    public async Task<IActionResult> Upload(IFormFile file)
    {
        if (file == null || file.Length == 0)
            return BadRequest("No file provided.");

        var allowed = new[] { ".pdf", ".docx", ".doc", ".txt", ".rtf" };
        var ext = Path.GetExtension(file.FileName).ToLowerInvariant();
        if (!allowed.Contains(ext))
            return BadRequest("File type not allowed.");

        if (file.Length > 20 * 1024 * 1024) // 20 MB limit
            return BadRequest("File too large.");

        var storedName = $"{Guid.NewGuid()}{ext}";
        var path = Path.Combine(_uploadsDir, storedName);

        await using (var fs = System.IO.File.Create(path))
        {
            await file.CopyToAsync(fs);
        }

        // Return both stored name and the physical path (or URL) you will use for DocumentViewer
        return Ok(new
        {
            fileName = storedName,
            physicalPath = path,
            // If you prefer to serve via an action:
            documentUrl = Url.Action(nameof(GetDocument), "Document", new { name = storedName }, Request.Scheme)
        });
    }

    // GET api/document/document/{name}
    [HttpGet("document/{name}")]
    public IActionResult GetDocument(string name)
    {
        // sanitize name: allow only filename characters (no ../)
        if (string.IsNullOrEmpty(name) || name.IndexOfAny(Path.GetInvalidFileNameChars()) >= 0)
            return BadRequest();

        var path = Path.Combine(_uploadsDir, name);
        if (!System.IO.File.Exists(path))
            return NotFound();

        // Return as octet-stream; TXTextControl may accept this or you can return appropriate content type
        return PhysicalFile(path, "application/octet-stream", enableRangeProcessing: true);
    }

    // POST api/document/save-signature?filename={storedName}
    // Accepts:
    //  - request body = raw document bytes (application/octet-stream)
    //  - form-file (multipart/form-data)
    //  - JSON { filename, contentBase64 }
    [HttpPost("save-signature")]
    [RequestSizeLimit(50 * 1024 * 1024)]
    public async Task<IActionResult> SaveSignature([FromQuery] string filename)
    {
        if (string.IsNullOrEmpty(filename))
            return BadRequest("filename query required.");

        // sanitize filename
        if (filename.IndexOfAny(Path.GetInvalidFileNameChars()) >= 0)
            return BadRequest("Invalid filename.");

        var destPath = Path.Combine(_uploadsDir, filename);

        try
        {
            // Case 1: multipart/form-data (TXTextControl may POST as form file)
            if (Request.HasFormContentType && Request.Form.Files.Count > 0)
            {
                var f = Request.Form.Files[0];
                await using (var fs = System.IO.File.Create(destPath))
                {
                    await f.CopyToAsync(fs);
                }
                return Ok(new { saved = true, path = destPath });
            }

            // Case 2: JSON body with base64 { "contentBase64": "...", "filename": "..." }
            if (Request.ContentType != null && Request.ContentType.Contains("application/json"))
            {
                using var sr = new StreamReader(Request.Body);
                var json = await sr.ReadToEndAsync();
                // naive parsing — prefer a model binding in real code
                // Example expects {"contentBase64":"..."}
                var obj = System.Text.Json.JsonSerializer.Deserialize<System.Text.Json.JsonElement>(json);
                if (obj.TryGetProperty("contentBase64", out var token))
                {
                    var b64 = token.GetString();
                    var bytes = Convert.FromBase64String(b64);
                    await System.IO.File.WriteAllBytesAsync(destPath, bytes);
                    return Ok(new { saved = true, path = destPath });
                }
            }

            // Case 3: raw bytes (application/octet-stream)
            // Save entire body to destPath
            await using (var outFs = System.IO.File.Create(destPath))
            {
                await Request.Body.CopyToAsync(outFs);
            }

            return Ok(new { saved = true, path = destPath });
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error saving signature");
            return StatusCode(500, "Save failed.");
        }
    }
  }
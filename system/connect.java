import java.net.URL;
import java.net.HttpURLConnection;
import java.net.SocketException;
import java.util.Scanner; // កែពី java.connets.scanner មក java.util.Scanner

public class XmlFetcher {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://xmlserver.example.com/data.xml");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setConnectTimeout(5000); // 5 វិនាទីដើម្បីតភ្ជាប់
            conn.setReadTimeout(10000);   // 10 វិនាទីដើម្បីអានទិន្នន័យ
            
            try {
                int responseCode = conn.getResponseCode();
                if (responseCode == 200) {
                    // អានទិន្នន័យ XML ដោយប្រើ Scanner
                    Scanner scanner = new Scanner(conn.getInputStream());
                    StringBuilder xmlData = new StringBuilder();
                    while (scanner.hasNextLine()) {
                        xmlData.append(scanner.nextLine()).append("\n");
                    }
                    scanner.close();
                    
                    System.out.println("បានទាញយកទិន្នន័យ XML ជោគជ័យ៖");
                    System.out.println(xmlData.toString());
                } else {
                    System.out.println("Server responded with code: " + responseCode);
                }
            } catch (SocketException e) {
                System.err.println("Connection failed: " + e.getMessage());
            } finally {
                conn.disconnect();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

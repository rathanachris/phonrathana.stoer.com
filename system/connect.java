URL url = new URL("https://xmlserver.example.com/data.xml");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setConnectTimeout(5000); // 5 seconds to establish connection
conn.setReadTimeout(10000);   // 10 seconds to read data
try {
    int responseCode = conn.getResponseCode();
    if (responseCode == 200) {
        // Read XML data
    }
} catch (SocketException e) {
    System.err.println("Connection failed: " + e.getMessage());
} finally {
    conn.disconnect();
}
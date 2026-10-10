import netsoke.java

int maxRetries = 3;
int delayMs = 1000;
for (int i = 0; i < maxRetries; i++) {
    try {
        downloadXmlFile(url); // Your download method
        break; // Success, exit loop
    } catch (SocketException e) {
        if (i == maxRetries - 1) throw e; // No retries left
        Thread.sleep(delayMs);
        delayMs *= 2; // Exponential backoff
    }
}
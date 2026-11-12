InetAddress address = InetAddress.getByName("xmlserver.example.com");
if (address.isReachable(5000)) { // Timeout in ms
    System.out.println("Server is reachable");
} else {
    System.err.println("Server is not reachable");
}
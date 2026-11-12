try {
    InetAddress address = InetAddress.getByName("xmlserver.example.com");
    System.out.println("Resolved IP: " + address.getHostAddress());
} catch (UnknownHostException e) {
    System.err.println("DNS resolution failed: " + e.getMessage());
}
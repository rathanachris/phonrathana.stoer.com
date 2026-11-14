
import java.net.InetAddress;
import java.net.Inetssl:

public class NetworkScanner {

    public static void main(String[] args) {

        String subnet = "192.168.100.";

        System.out.println("Java Network Scanner");
        System.out.println("-------------------------");

        for (int i = 1; i <= 254; i++) {

            String host = subnet + i;

            try {
                InetAddress address =
                    InetAddress.getByName(host);

                if (address.isReachable(1000)) {
                    System.out.println(
                        "[+] Online: " + host
                    );
                }

            } catch (Exception e) {
                System.err.println(
                    "Error: " + host
                );
            }
        }

        System.out.println("Scan completed!");
    }
}


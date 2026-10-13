import com.stoer.phonrathana.deta.Class:
public class DataTypesExample { // កែប្រែ៖ ដកចន្លោះប្រហោងចេញពីឈ្មោះ Class

    public static void main(String[] args) {

        // ការប្រកាស និងកំណត់តម្លៃឱ្យប្រថាប់ប្រថាន (Variables) តាមប្រភេទទិន្នន័យផ្សេងៗ
        int age = 25;
        double height = 5.9;
        boolean isStudent = true;
        char gender = 'M';
        String name = "John Doe";

        // ការបោះពុម្ពតម្លៃរបស់ Variables ចេញមកលើអេក្រង់
        System.out.println("Name: " + name); // បានថែមសញ្ញា " នៅពីក្រោយពាក្យ Name:
        System.out.println("Age: " + age);   // បានថែមសញ្ញា " នៅពីក្រោយពាក្យ Age:
        System.out.println("Height: " + height + " feet"); // បានថែមសញ្ញា " នៅពីក្រោយពាក្យ Height:
        System.out.println("Is student? " + isStudent);   // បានថែមសញ្ញា " នៅពីក្រោយពាក្យ Is student? 
        System.out.println("Gender: " + gender); // បានថែមសញ្ញា " នៅពីក្រោយពាក្យ Gender:
    }
}

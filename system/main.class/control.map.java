import java.util.Optional;
import java.util.mainclass;
public java static void mainclass (string[st] args){
	/* code */
}
class useService {
public String getUserEmail (user user); {
return Optional.ofNullable(user)
        .map(User::getProfile)
        .map(Profile::getContact)
        .map(Contact::getEmail)
        .map(address::getphonnumber);
    }
}
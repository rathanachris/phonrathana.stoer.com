Person john = Person.newBuilder()
    .setId(1234)
    .setName("phonrathana")
    .setEmail("admain@phonrathanaprtner.com")
    .build();
output = new FileOutputStream(args[0]);
john.writeTo(output);

imena = [];
godine = [];
unos = [];
i = 0;
switch = True;
while switch:
    print("\nOsoba broj", i+1);
    imena.append(str(input("Unesite ime osobe: ")));
    godine.append(int(input("Njihove godine: ")));
    # unos.append(tuple(imena[i], godine[i]));

    unos.append(list([imena[i], godine[i]]));
    print("\Da li zelite da unesete jos jednu osobu? y/n");
    odgovor = str(input(""));
    if(odgovor == "n"):
        switch = False;
    elif(odgovor == "y"):
        i += 1;
    else:
        print("Uneli ste nevezeci odgovor");
        switch = False;

print(unos);

parovi = [{"Name": key,  "age" : value} for (key, value) in unos];

print(parovi);


### Create output directories

05/27 by [@mjohn218](https://github.com/mjohn218)

Referenced [commit](https://github.com/mjohn218/nerdss_development/commit/f4bd6514437ac3311148f141435c6ffad541cb38)
____________

- Include `stat.h` package
```cpp
#include <sys/stat.h>
```
- Use `mkdir` function in the format of
```cpp
mkdir(filename_string, access_code);
// return true if directory is successfully created
```
- Example in [NERDSS](https://github.com/mjohn218/nerdss_development/commit/f4bd6514437ac3311148f141435c6ffad541cb38#diff-a8351967ac28f8ef7bdd757e29b568681d26ce40ac94975755a58bdbb6e43600)
```cpp
if (mkdir("PDB", 0777) == -1) {
    std::cerr << "Error :  " << strerror(errno) << std::endl;
} else {
    std::cout << "Directory created";
}
if (mkdir("RESTARTS", 0777) == -1) {
    std::cerr << "Error :  " << strerror(errno) << std::endl;
} else {
    std::cout << "Directory created";
}
```
- Access code `0777` means granting reading / writing / executing access to everybody (owner, group, and other users). [Reference](https://digitalfortress.tech/php/difference-file-mode-0777-vs-777/)

![image](https://user-images.githubusercontent.com/44514233/172945323-e13c4fe7-add6-46bc-99ce-5bde6d33ea30.png)

- Remember to change directories in IO lines accordingly:
```cpp
sprintf(fnameProXYZ, "RESTARTS/restart%lld.dat", simItr);
```

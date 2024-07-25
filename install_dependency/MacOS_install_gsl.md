To install the GNU Scientific Library (GSL) using Homebrew on a macOS system, you can follow these steps:

1. **Install Homebrew**: If you don't have Homebrew installed yet, you can install it by running the following command in your terminal:

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Update Homebrew**: Before installing any new package, it's a good practice to update Homebrew to ensure you have the latest package information:

    ```sh
    brew update
    ```

3. **Install GSL**: Once Homebrew is updated, you can install the GSL package with the following command:

    ```sh
    brew install gsl
    ```

4. **Verify Installation**: After the installation is complete, you can verify that GSL has been installed correctly by checking its version:

    ```sh
    gsl-config --version
    ```

### Example:

```sh
# Step 1: Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Step 2: Update Homebrew
brew update

# Step 3: Install GSL
brew install gsl

# Step 4: Verify the installation
gsl-config --version
```

### Additional Information:

- **GSL Documentation**: You can find more information about GSL and its usage in the [official GSL documentation](https://www.gnu.org/software/gsl/doc/).
- **Homebrew Documentation**: For more details about using Homebrew, you can refer to the [Homebrew documentation](https://docs.brew.sh/).

By following these steps, you should have GSL installed on your macOS system using Homebrew, allowing you to use its scientific computation capabilities in your projects.

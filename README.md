# PF2Downloader
To end-users, this tool is the official installer and updater for Pre-Fortress 2. 

To programmers, this is a thin and rough script that sits on top of Aria2 and Butler to provide reasonably-efficient updating without too much complication. 

To other Sourcemods, this is a tool you can use for *your project* with only minor work, as the mechanism here is extremely agnostic and flexible.

## Development
You must install dependencies by running the following command.
```
pip install -r requirements.txt
```

PyInstaller is used to build this into a single-file binary and a `.spec` configuration file is included.
PyBabel can generate the localization files by configuring and running `GeneratePOT.sh` followed by `GenerateMO.sh` on both Windows and Linux using Bash Shell.

For convenience in building, the `Binaries` folder contains prebuilt and static versions of Aria2 and Butler for Windows and Linux. 
- The static build of Aria2 can be found on this [archived release.](https://github.com/q3aql/aria2-static-builds/releases)
- The official build of Butler is [supplied by itch.io.](https://itchio.itch.io/butler)

We have provided CI/CD scripts in the `.github` folder for building and releasing the installer for both Windows and Linux. They can be customized with slight configuration.

----

<a href="https://hosted.weblate.org/engage/pf2downloader/">
<img src="https://hosted.weblate.org/widgets/pf2downloader/-/287x66-grey.png" alt="Translation status" />
</a>

### Creates logs for a list of MongoDB server versions

`create_mongodb_logs.py` executes a JavaScript file with CRUD operations against a list of MongoDB server versions. The goal is to try to identify differences in logging across major (or minor) releases of MongoDB, which can be useful for authors developing log parsing tools.

The MongoDB server logs generated will be saved in an output directory structure along with the `mongod.conf` file used.

<pre>
usage: create_mongodb_logs.py [-h][-m MONGO_CONFIG] [-v VERSIONS] [-o OUTPUT_DIR] [-j JSCRIPT]

Optional arguments:
-h, --help            show this help message and exit
  -m MONGO_CONFIG, --mongo_config MONGO_CONFIG
      Path to mongod.conf with configuration. Default is
      ./mongod.conf
  -v VERSIONS, --versions VERSIONS
      Path to JSON file with versions. Default is
      ./versions.json
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
      Path to directory where logs will be stored. Defaults to .
  -j JSCRIPT, --jscript JSCRIPT
      Path to JavaScript file to execute.
</pre>

The file `versions.json` must have a list of versions and paths as follows:

<pre>
 [
   {
     "name": "3.0.12",
     "path": "/usr/local/m/versions/3.0.12/bin"
   },
   {
     "name": "3.2.13",
     "path": "/usr/local/m/versions/3.2.13/bin"
   },
   {
     "name": "3.4.7-ent",
     "path": "/usr/local/m/versions/3.4.7-ent/bin"
   }
 ]

</pre>

### Limitations

There is currently no capability to directly download MongoDB server binaries; any required binaries must exist in the `path` specified in your `versions.json` file. A recommended tool to help download multiple versions of MongoDB for testing is the [`m` MongoDB version manager](https://www.npmjs.com/package/m).  `m` downloads binaries into a directory structure using paths similar to the example `versions.json` above.
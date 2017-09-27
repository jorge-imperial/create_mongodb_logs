**Creates logs for a list of MongoDB versions.**


Using a list of versions specified in a file, runs a script with CRUD operations. The logs generated will be saved in a directory structure, along with the mongod.conf file used.


usage: create_mongo_logs.py [-h] [-m MONGO_CONFIG] [-v VERSIONS]
                            [-o OUTPUT_DIR] [-j JSCRIPT]

Create mongod.log files for different versions of mongod.

optional arguments:
  -h, --help            show this help message and exit
  -m MONGO_CONFIG, --mongo_config MONGO_CONFIG
                        Path to mongod.conf with configuration. Default is
                        ./mongod.conf
  -v VERSIONS, --versions VERSIONS
                        Path to json file with versions. Default is
                        ./versions.json
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Path to directory where logs will be stored. Defaults
                        to .
  -j JSCRIPT, --jscript JSCRIPT
                        Path to javascript file to execute.
                        
                        
The file versions.json must have a list of versions and paths as folows:

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


The binaries can be downloaded previously with [m](). There is currently no capability to download directly the binaries.

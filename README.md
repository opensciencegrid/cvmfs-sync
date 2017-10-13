CVMFS-Sync Services
===================

The CVMFS-Sync package includes all the services for dynamic automated repositories hosted
currently at hcc-cvmfs-repo.unl.edu.


Override SystemD Services
-------------------------

It is common that the defaults in this package may not be appropriate.  Therefore, you may override
the SystemD services by creating specially crafted files.

For example, we can override the default of the `nova-data-update.service` service by creating 
the directory and file `/etc/systemd/system/nova-data-update.service.d/override.conf`.  It will contain:

    [Service]
    User=nova

Since CVMFS requires the same user for every transaction, it will likely be necessary to override the user
default that is in the service file.

License
-------

   Copyright 2017 Derek Weitzel

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.



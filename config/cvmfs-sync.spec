Name:           cvmfs-sync
Version:        3.2
Release:        1%{?dist}
Summary:        CVMFS Sync

License:        ASL 2.0
URL:            https://github.com/bbockelm/cvmfs-sync
# Generated from:
# git archive --format=tgz --prefix=%{name}-%{version}/ v%{version} > %{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz

Requires:       cvmfs-server
Requires:	xrootd-python
Requires(pre): 	shadow-utils

%{?systemd_requires}
BuildRequires: systemd

BuildArch: 	noarch

%description
Various scripts to help synchronize *.osgstorage.org repositories to CVMFS.

%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

# Install update scripts
install -d $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync
#install -m 0755 update-scripts/* $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/
install -m 0755 bin/cvmfs_sync $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/cvmfs_sync
install -m 0755 bin/ligo-auth-gen $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/ligo-auth-gen
install -m 0755 update-scripts/cvmfs-sync-driver $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/cvmfs-sync-driver

# Install the SystemD unit files
install -d $RPM_BUILD_ROOT/%{_unitdir}
install -m 0600 config/cvmfs-data-update@.service $RPM_BUILD_ROOT/%{_unitdir}/

# Install the authorization files.
install -d $RPM_BUILD_ROOT/%{_datarootdir}/cvmfs-sync
install -m 0644 config/ligo_authz config/cms_authz $RPM_BUILD_ROOT/%{_datarootdir}/cvmfs-sync

# Install the cvmfs-sync config
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/cvmfs-sync
install -m 0644 config/*.config $RPM_BUILD_ROOT/%{_sysconfdir}/cvmfs-sync/

# Make sure the cache directory is pre-created.
install -d $RPM_BUILD_ROOT/%{_localstatedir}/cache/cvmfs-sync

%pre
# Install the cvmfs-sync user
getent group cvmfs-sync >/dev/null || groupadd -r cvmfs-sync
getent passwd cvmfs-sync >/dev/null || \
    useradd -r -g cvmfs-sync -d /var/lib/cvmfs-sync -s /sbin/nologin \
    -c "User to synchronize CVMFS with a remote XRootD server namespace" cvmfs-sync
exit 0


%post
%systemd_post cvmfs-data-update@.service


%preun
%systemd_preun cvmfs-data-update@.service


%postun
%systemd_postun cvmfs-data-update@.service


%files
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/cvmfs_sync
%{_libexecdir}/%{name}/ligo-auth-gen
%{_libexecdir}/%{name}/cvmfs-sync-driver
%dir %attr(0755, cvmfs-sync, cvmfs-sync) %{_datarootdir}/%{name}
%dir %attr(0755, cvmfs-sync, cvmfs-sync) %{_localstatedir}/cache/%{name}
%{_datarootdir}/%{name}/cms_authz
%{_datarootdir}/%{name}/ligo_authz
%{_unitdir}/cvmfs-data-update@.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/cms.osgstorage.org.config
%config(noreplace) %{_sysconfdir}/%{name}/des.osgstorage.org.config
%config(noreplace) %{_sysconfdir}/%{name}/ligo.osgstorage.org.config
%config(noreplace) %{_sysconfdir}/%{name}/mu2e.osgstorage.org.config
%config(noreplace) %{_sysconfdir}/%{name}/nova.osgstorage.org.config
%config(noreplace) %{_sysconfdir}/%{name}/stash.osgstorage.org.config
%config(noreplace) %{_sysconfdir}/%{name}/uboone.osgstorage.org.config

%doc


%changelog
* Tue Oct 31 2017 Brian Bockelman - 3.2-1
- Fix automated periodic GC runs.

* Tue Oct 17 2017 Brian Bockelman - 3.1-1
- Fixup various config file typos.

* Tue Oct 17 2017 Brian Bockelman - 3.0-1
- Complete overhaul of driver scripts for cvmfs-sync repos.

* Sat Oct 14 2017 Brian Bockelman - 2.2-1
- Unify all data update scripts to use cvmfs_sync.

* Fri Oct 13 2017 Brian Bockelman - 2.1-1
- Include authz files into the RPM.

* Fri Oct 13 2017 Brian Bockelman - 2.0-2
- Properly handle systemd deps.

* Fri Oct 13 2017 Brian Bockelman - 2.0-1
- Integrate new CMS sync script into release.


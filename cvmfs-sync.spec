Name:           cvmfs-sync
Version:        1.0
Release:        1%{?dist}
Summary:        CVMFS Sync

License:        ASL 2.0
URL:            https://github.com/bbockelm/cvmfs-sync
Source0:        cvmfs-sync-%{version}.tar.gz

Requires:       cvmfs-server
Requires:	xrootd-python
Requires(pre): 	shadow-utils

BuildArch: 	noarch

%description


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 bin/stash_async $RPM_BUILD_ROOT/%{_bindir}/stash_async
install -m 0755 bin/cvmfs_sync $RPM_BUILD_ROOT/%{_bindir}/cvmfs_sync

# Install update scripts
install -d $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync
install -m 0755 update-scripts/* $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/

install -d $RPM_BUILD_ROOT/%{_datarootdir}/cvmfs-sync
install -m 0755 ligo-auth-gen $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/ligo-auth-gen

# Install the SystemD unit files
install -d $RPM_BUILD_ROOT/%{_unitdir}
install -m 0600 config/*.service $RPM_BUILD_ROOT/%{_unitdir}/

%pre
# Install the cvmfs-sync user
getent group cvmfs-sync >/dev/null || groupadd -r cvmfs-sync
getent passwd cvmfs-sync >/dev/null || \
    useradd -r -g cvmfs-sync -d /usr/share/cvmfs-sync -s /sbin/nologin \
    -c "User to synchronize CVMFS with a remote XRootD server namespace" cvmfs-sync
exit 0


%files
%{_libexecdir}/cvmfs-sync
%{_bindir}/*
%dir %attr(0555, cvmfs-sync, cvmfs-sync) %{_datarootdir}/cvmfs-sync
%{_unitdir}/*


%doc



%changelog

Name:           cvmfs-sync
Version:        1.0
Release:        1%{?dist}
Summary:        CVMFS Sync

License:        ASL 2.0
URL:            
Source0:        

BuildRequires:  
Requires:       
Requires(pre): shadow-utils

%description


%prep
%setup -q


%build
#%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 bin/stash-async $RPM_BUILD_ROOT/%{_bindir}/stash-async
install -m 0755 bin/cvmfs-sync $RPM_BUILD_ROOT/%{_bindir}/cvmfs-sync

# Install update scripts
install -d $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync
install -m 0755 update-scripts/* $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/

install -d $RPM_BUILD_ROOT/%{_datarootdir}/cvmfs-sync
install -m 0755 ligo-auth-gen $RPM_BUILD_ROOT/%{_libexecdir}/ligo-auth-gen

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
%{_datarootdir}/cvmfs-sync



%doc



%changelog

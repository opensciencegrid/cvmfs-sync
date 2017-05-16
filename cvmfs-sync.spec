Name:           cvmfs-sync
Version:        1.0
Release:        1%{?dist}
Summary:        CVMFS Sync

License:        ASL 2.0
URL:            
Source0:        

BuildRequires:  
Requires:       

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync
install -m 0755 stash-async $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/stash-async
install -m 0755 cvmfs-sync $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/cvmfs-sync
install -m 0755 *update $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/


%files
%{_libexecdir}/cvmfs-sync



%doc



%changelog

Name:           cvmfs-sync
Version:        2.2
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

install -d $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 bin/cvmfs_sync $RPM_BUILD_ROOT/%{_bindir}/cvmfs_sync

# Install update scripts
install -d $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync
install -m 0755 update-scripts/* $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/

install -m 0755 bin/ligo-auth-gen $RPM_BUILD_ROOT/%{_libexecdir}/cvmfs-sync/ligo-auth-gen

# Install the SystemD unit files
install -d $RPM_BUILD_ROOT/%{_unitdir}
install -m 0600 config/*.service $RPM_BUILD_ROOT/%{_unitdir}/

# Install the authorization files.
install -d $RPM_BUILD_ROOT/%{_datarootdir}/cvmfs-sync
install -m 0644 config/ligo_authz config/cms_authz $RPM_BUILD_ROOT/%{_datarootdir}/cvmfs-sync

%pre
# Install the cvmfs-sync user
getent group cvmfs-sync >/dev/null || groupadd -r cvmfs-sync
getent passwd cvmfs-sync >/dev/null || \
    useradd -r -g cvmfs-sync -d /usr/share/cvmfs-sync -s /sbin/nologin \
    -c "User to synchronize CVMFS with a remote XRootD server namespace" cvmfs-sync
exit 0


%post
%systemd_post cms-data-update.service
%systemd_post ligo-data-update.service
%systemd_post nova-data-update.service
%systemd_post des-data-update.service
%systemd_post mu2e-data-update.service
%systemd_post stash-data-update.service
%systemd_post uboone-data-update.service


%preun
%systemd_preun cms-data-update.service
%systemd_preun ligo-data-update.service
%systemd_preun nova-data-update.service
%systemd_preun des-data-update.service
%systemd_preun mu2e-data-update.service
%systemd_preun stash-data-update.service
%systemd_preun uboone-data-update.service


%postun
%systemd_postun cms-data-update.service
%systemd_postun ligo-data-update.service
%systemd_postun nova-data-update.service
%systemd_postun des-data-update.service
%systemd_postun mu2e-data-update.service
%systemd_postun stash-data-update.service
%systemd_postun uboone-data-update.service


%files
%{_libexecdir}/cvmfs-sync
%{_bindir}/cvmfs_sync
%dir %attr(0755, cvmfs-sync, cvmfs-sync) %{_datarootdir}/cvmfs-sync
%{_datarootdir}/cvmfs-sync/cms_authz
%{_datarootdir}/cvmfs-sync/ligo_authz
%{_unitdir}/*


%doc


%changelog
* Sat Oct 14 2017 Brian Bockelman - 2.2-1
- Unify all data update scripts to use cvmfs_sync.

* Fri Oct 13 2017 Brian Bockelman - 2.1-1
- Include authz files into the RPM.

* Fri Oct 13 2017 Brian Bockelman - 2.0-2
- Properly handle systemd deps.

* Fri Oct 13 2017 Brian Bockelman - 2.0-1
- Integrate new CMS sync script into release.


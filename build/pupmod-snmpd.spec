Summary: SNMP Puppet Module
Name: pupmod-snmpd
Version: 4.1.0
Release: 3
License: Apache License, Version 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: pupmod-common >= 2.1.2-2
Requires: pupmod-concat >= 2.0.0-0
Requires: pupmod-functions >= 2.0.0-0
Requires: pupmod-rsync >= 2.0.0-0
Requires: puppet >= 3.3.0
Requires: puppetlabs-stdlib
Requires: simp_bootstrap >= 2.0.0-0
Requires: simp_rsync_filestore >= 2.0.0-0
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Provides: pupmod-snmp
Obsoletes: pupmod-snmp
Obsoletes: pupmod-snmpd-test

Prefix:"/etc/puppet/environments/simp/modules"

%description
This module provides fully templated net-snmp functionality.
It does require that an 'snmp' rsync area be shared to the clients.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/snmpd

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/snmpd
done

mkdir -p %{buildroot}/usr/share/simp/tests/modules/snmpd

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/snmpd

%files
%defattr(0640,root,puppet,0750)
/etc/puppet/environments/simp/modules/snmpd

%post
#!/bin/sh

if [ -d /etc/puppet/environments/simp/modules/snmpd/plugins ]; then
  /bin/mv /etc/puppet/environments/simp/modules/snmpd/plugins /etc/puppet/environments/simp/modules/snmpd/plugins.bak
fi

%postun
# Post uninstall stuff

%changelog
* Fri Jan 16 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-3
- Changed puppet-server requirement to puppet

* Sun Jun 22 2014 Kendall Moore <kmoore@keywcorp.com> - 4.1.0-2
- Removed MD5 file checksums for FIPS compliance.

* Mon May 19 2014 Kendall Moore <kmoore@keywcorp.com> - 4.1.0-1
- Removed stock classes and corresponding spec tests so they can be ported to the SIMP module.

* Wed Apr 30 2014 Kendall Moore <kmoore@keywcorp.com> - 4.1.0-0
- Refactored all manifests to pass lint tests.
- Removed all singleton defines.
- Added spec tests.

* Tue Apr 22 2014 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-0
- Updated to use hiera to replace all globals.

* Thu Feb 13 2014 Kendall Moore <kmoore@keywcorp.com> - 2.0.1-2
- Updated all boolean strings to native booleans.

* Mon Oct 07 2013 Kendall Moore <kmoore@keywcorp.com> - 2.0.1-1
- Updated all erb templates to properly scope variables.

* Fri Jul 26 2013 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.1-0
- Changed all calls to file_line to simp_file_line.

* Mon Feb 25 2013 Maintenance
2.0.0-9
- Added a call to $::rsync_timeout to the rsync call since it is now required.
- Edited the Cucumber test to include correct class.

* Mon Jan 07 2013 Maintenance
2.0.0-8
- Created a Cucumber test to install and configure an snmpd stock server
  and ensure that the snmpd service is running.

* Wed Apr 11 2012 Maintenance
2.0.0-7
- Now use the Puppet Labs stdlib function 'file_line' instead of
  'functions::append_if_no_such_line'
- Moved mit-tests to /usr/share/simp...
- Updated pp files to better meet Puppet's recommended style guide.

* Fri Mar 02 2012 Maintenance
2.0.0-6
- Improved test stubs.

* Mon Dec 19 2011 Maintenance
2.0.0-5
- Updated the spec file to not require a separate file list.
- Added a '1' after dontLogTCPWrappersConnects to make it actually take effect.

* Mon Dec 05 2011 Maintenance
2.0.0-4
- No longer restart snmpd every time an rsync happens. This was due to the
  extended ACLs getting overwritten which should not have been done.

* Mon Nov 14 2011 Maintenance
2.0.0-3
- Updated to add a stock class and fix some issues with running as a non-root
  user. Snmpd now runs as snmpd/snmpd by default under uid/gid 333.

* Mon Oct 10 2011 Maintenance
2.0.0-2
- Updated to put quotes around everything that need it in a comparison
  statement so that puppet > 2.5 doesn't explode with an undef error.

* Fri Feb 11 2011 Maintenance - 2.0.0-1
- Changed all instances of defined(Class['foo']) to defined('foo') per the
  directions from the Puppet mailing list.
- Updated to use rsync native type
- Updated to use concat_build and concat_fragment types.

* Tue Jan 11 2011 Maintenance
2.0.0-0
- Refactored for SIMP-2.0.0-alpha release

* Fri Nov 05 2010 Maintenance - 1.0-3
- /etc/snmp/snmpd.conf is now owned by root.snmp

* Tue Oct 26 2010 Maintenance - 1.0-2
- Converting all spec files to check for directories prior to copy.

* Thu Sep 09 2010 Maintenance
1.0-1
- Replaced tcpwrappers::tcpwrappers_allow with tcpwrappers::allow.

* Tue May 25 2010 Maintenance
1.0-0
- Renamed the snmp module to snmpd as it should have been to begin with.

* Tue Apr 27 2010 Maintenance
0.1-3
- Had misplaced '$' signs in the main define.

* Thu Jan 28 2010 Maintenance
0.1-2
- Now ensure that all snmp templates pre-fill return string values. Previously,
  this could have ended up with a 'nil' evaluation and execution falut.

* Mon Nov 02 2009 Morgan Haskel <morgan.haskel@onyxpoint.com> - 0.1-1
- Tested version with all modules.
- SNMPD should be fully templated.
- snmptrapd has not yet been covered.

* Tue Oct 20 2009 Morgan Haskel <morgan.haskel@onyxpoint.com> - 0.1-0
- Initial Release

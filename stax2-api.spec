Name:             stax2-api
Version:          3.1.1
Release:          10%{?dist}
Summary:          Experimental API extending basic StAX implementation
License:          BSD
Group:            Development/Libraries
URL:              http://docs.codehaus.org/display/WSTX/StAX2
BuildArch:        noarch

Source0:          http://repository.codehaus.org/org/codehaus/woodstox/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:          http://repository.codehaus.org/org/codehaus/woodstox/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires:    maven-local
BuildRequires:    bea-stax-api

%description
StAX2 is an experimental API that is intended to extend
basic StAX specifications in a way that allows implementations
to experiment with features before they end up in the actual
StAX specification (if they do). As such, it is intended
to be freely implementable by all StAX implementations same way
as StAX, but without going through a formal JCP process.


%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c %{name}
# fixing incomplete source directory structure
mkdir -p src/main/java
mv -f org src/main/java/
cp %{SOURCE1} pom.xml
%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.1.1-10
- Mass rebuild 2013-12-27

* Tue Aug 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-9
- Migrate away from mvn-rpmbuild

* Wed Jul 31 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1.1-8
- Rebuild for new sources

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 29 2011 Jaromir Capik <jcapik@redhat.com> - 3.1.1-2
- bea-stax has it's own depmap now -> removing the local one

* Tue Sep 13 2011 Jaromir Capik <jcapik@redhat.com> - 3.1.1-1
- Initial version

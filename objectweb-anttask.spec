%include	/usr/lib/rpm/macros.java
Summary:	ObjectWeb Ant task
Summary(pl.UTF-8):	Zadanie Anta ObjectWeb
Name:		objectweb-anttask
Version:	1.3.2
Release:	1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://download.forge.objectweb.org/monolog/ow_util_ant_tasks_%{version}.zip
# Source0-md5:	cd602bf75a0feab480fa97739955b84e
Patch0:		%{name}-ant.patch
URL:		http://forge.objectweb.org/projects/monolog/
BuildRequires:	ant >= 1.7
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	xalan-j
Requires:	ant >= 1.7
# for dependency component
Suggests:	asm2 >= 2.1
#Provides:	owanttask
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObjectWeb Ant task.

%description -l pl.UTF-8
Zadanie Anta ObjectWeb.

%prep
%setup -c -q -n %{name}
%patch0 -p1

find output -name '*.class' | xargs rm -f
rm externals/ant.jar

%build
# use bundled asm-2.1 for build to avoid loop (asm2 BR: objectweb-anttask)
required_jars="xalan"
export CLASSPATH="$(build-classpath $required_jars):externals/asm-2.1.jar"
%ant jar \
	-Dbuild.compiler=modern

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
install output/lib/ow_util_ant_tasks.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

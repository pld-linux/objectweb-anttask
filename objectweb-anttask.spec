%include	/usr/lib/rpm/macros.java
Summary:	ObjectWeb Ant task
Summary(pl.UTF-8):	Zadanie Anta ObjectWeb
Name:		objectweb-anttask
Version:	1.2
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://download.forge.objectweb.org/monolog/ow_util_ant_tasks_%{version}.zip
# Source0-md5:	59ec69d435aedeeb710229fddf5fd34c
Patch0:		%{name}-source.patch
URL:		http://forge.objectweb.org/projects/monolog/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	xalan-j
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
find -name '*.class' -o -name '*.jar' | xargs rm -rf

%build
required_jars="xalan"
export CLASSPATH=$(build-classpath $required_jars)
%ant jar \
	-Dcompile.source=1.4 \
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

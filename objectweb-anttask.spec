Summary:	ObjectWeb Ant task
Name:		objectweb-anttask
Version:	1.2
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
URL:		http://forge.objectweb.org/projects/monolog/
BuildArch:	noarch
Source0:	http://download.forge.objectweb.org/monolog/ow_util_ant_tasks_1.2.zip
# Source0-md5:	59ec69d435aedeeb710229fddf5fd34c
BuildRequires:	jakarta-ant
BuildRequires:	jdk
#Provides:	owanttask
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObjectWeb Ant task

%prep
%setup -c -q -n %{name}
find . -name "*.class" -exec rm {} \;
find . -name "*.jar" -exec rm {} \;

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
export CLASSPATH=
ant -Dbuild.compiler=modern jar

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}

install output/lib/ow_util_ant_tasks.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*

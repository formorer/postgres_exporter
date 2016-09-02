Name:           postgres_exporter   
Version:        0.0.1
Release:        1%{?dist}
Summary:        postgres_exporter for prometheus
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        postgres_exporter
Source1:        postgres_exporter.service
Source2:        postgres_exporter.default
License:        GPL


%description
Prometheus Exporter for postgres metrics 

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system/
mkdir -p $RPM_BUILD_ROOT/etc/default/
install -m 755 %{_sourcedir}/postgres_exporter $RPM_BUILD_ROOT/usr/bin
install -m 644 %{_sourcedir}/postgres_exporter.service $RPM_BUILD_ROOT/lib/systemd/system/
cp %{_sourcedir}/postgres_exporter.default $RPM_BUILD_ROOT/etc/default/postgres_exporter 

%files
/lib/systemd/system/postgres_exporter.service
/usr/bin/postgres_exporter
%attr(0640,postgres,postgres) /etc/default/postgres_exporter

%doc



%changelog

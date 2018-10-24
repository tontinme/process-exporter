Name: 		process-exporter
Version:	0.3.10
Release:	1%{?dist}
Summary:	Prometheus exporter that mines /proc to report on selected processes
License:	MIT
URL:		https://github.com/ncabatoff/process-exporter
Source0:	process-exporter-%{version}.tar.gz

#BuildRequires:	golang
BuildRequires:	systemd

Requires(pre):	shadow-utils	
Requires(post):	systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Prometheus exporter that mines /proc to report on selected processes

%prep
%setup -q -n %{name}-%{version}

%build

%install
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name}
install -D -p -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -D -p -m 0644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service
install -m 644 -t %{buildroot}/%{_sysconfdir}/%{name} process.yml

# create /var/lib/process-exporter
install -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}

%check
# empty for now

%pre

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%dir %attr(-,root,root) %{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service

Name: edk2
Summary: edk2 XXX
Version: 0.1
Release: 1

Group: Development/Tools
License: GPLv2
URL: http://fixmeXXX.xen.org/gitweb/?p=ovmf.git
Source0: https://code.citrite.net/rest/archive/latest/projects/~ROSSLA/repos/%{name}/archive?at=master&format=tar.gz#/%{name}.tar.gz

BuildRequires: nasm
BuildRequires: libuuid-devel
BuildRequires: python
BuildRequires: iasl


%description
OVMF XXX


%prep
%autosetup -p1


%build
OvmfPkg/build.sh -D SECURE_BOOT_ENABLE -a X64 -b DEBUG -n %{?_smp_flags}


%install
install -m 755 -d %{buildroot}/%{_datadir}/%{name}
install -m 644 Build/OvmfX64/DEBUG_GCC*/FV/OVMF_CODE.fd %{buildroot}/%{_datadir}/%{name}/ovmf.bin
install -m 644 Build/OvmfX64/DEBUG_GCC*/FV/OVMF_VARS.fd %{buildroot}/%{_datadir}/%{name}/ovmf-vars.bin


%files
%{_datadir}/%{name}


%changelog

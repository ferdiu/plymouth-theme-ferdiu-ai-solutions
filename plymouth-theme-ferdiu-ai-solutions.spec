Name:           plymouth-theme-ferdiu-ai-solutions
Version:        1.0
Release:        1%{?dist}
Summary:        Spinner plymouth theme branded for ferdiu AI solutions

License:        MIT AND LicenseRef-Logo-Proprietary
URL:            https://github.com/ferdiu/plymouth-theme-ferdiu-ai-solutions

Source0:        https://github.com/ferdiu/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       plymouth
Requires(post): plymouth
Requires(post): dracut
Requires(postun): plymouth
Requires(postun): dracut

%description
A branded variant of the Fedora spinner plymouth theme.

Visually identical to the default spinner theme,
but replaces the watermark logo and metadata with
ferdiu AI solutions branding.

Author: Federico Manzella

%prep
%autosetup -n %{name}-%{version}

%build
# nothing to build

%install
rm -rf %{buildroot}

# Install theme directory
install -d %{buildroot}%{_datadir}/plymouth/themes/ferdiu-ai-solutions

cp -a %{_datadir}/plymouth/themes/spinner/* \
   %{buildroot}%{_datadir}/plymouth/themes/ferdiu-ai-solutions/

# Replace watermark
install -m 0644 ferdiu-ai-solutions-logo.png \
    %{buildroot}%{_datadir}/plymouth/themes/ferdiu-ai-solutions/watermark.png

# Patch metadata + accent color
sed -i \
    -e 's/^Name\(.*\)=.*/Name\1=ferdiu AI solutions/' \
    -e 's/^Description\(.*\)=.*/Description\1=Spinner theme branded for ferdiu AI solutions/' \
    -e 's/^ProgressBarForegroundColor=.*/ProgressBarForegroundColor=0xb875dc/' \
    %{buildroot}%{_datadir}/plymouth/themes/ferdiu-ai-solutions/spinner.plymouth

# Rename descriptor
mv %{buildroot}%{_datadir}/plymouth/themes/ferdiu-ai-solutions/spinner.plymouth \
   %{buildroot}%{_datadir}/plymouth/themes/ferdiu-ai-solutions/ferdiu-ai-solutions.plymouth

%post
plymouth-set-default-theme ferdiu-ai-solutions >/dev/null 2>&1 || :
dracut -f >/dev/null 2>&1 || :

%postun
if [ $1 -eq 0 ]; then
    plymouth-set-default-theme spinner >/dev/null 2>&1 || :
    dracut -f >/dev/null 2>&1 || :
fi

%files
%license NOTICE
%license LICENSE
%license LICENSE-LOGO
%doc README.md
%{_datadir}/plymouth/themes/ferdiu-ai-solutions

%changelog
* Sat Feb 21 2026 Federico Manzella <ferdiu.manzella@gmail.com> - 1.0-1
- Initial COPR-ready release
- Based on Fedora spinner theme
- Replaced watermark
- Updated metadata
- Accent color #b875dc

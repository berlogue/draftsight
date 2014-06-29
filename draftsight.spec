%define __os_install_post %{nil}
%define debug_package %{nil}
%define dsver V1R5.1

Summary:	Professional CAD system: supported file formats are DWT, DXF and DWG
Name:		draftsight
Version:	2014.3.70
Release:	2%{?dist}.2

License:	Standalone license, activation required
URL:		http://www.3ds.com/products-services/draftsight/download-draftsight
Source0:	http://dl-ak.solidworks.com/nonsecure/draftsight/%{dsver}/draftSight.rpm

BuildRequires:	desktop-file-utils

#Requires:	/bin/bash
#Requires:	/bin/sh
#Requires:	libAecGeometry.so.1
#Requires:	libDDKERNEL.so.1
#Requires:	libDwfCore.so.1
#Requires:	libDwfToolkit.so.1
#Requires:	libFXCommandsBase.so.1
#Requires:	libFXCrashRpt.so.1
#Requires:	libFXExport.so.1
#Requires:	libFXLISP.so.1
#Requires:	libFXRenderBase.so.1
#Requires:	libFxFileDialogs.so.1
#Requires:	libFxImages.so.1
#Requires:	libQtCore.so.4
#Requires:	libQtDBus.so.4
#Requires:	libQtGui.so.4
#Requires:	libQtHelp.so.4
#Requires:	libQtMultimedia.so.4
#Requires:	libQtNetwork.so.4
#Requires:	libQtOpenGL.so.4
#Requires:	libQtSql.so.4
#Requires:	libQtSvg.so.4
#Requires:	libQtWebKit.so.4
#Requires:	libQtXml.so.4
#Requires:	libQtXmlPatterns.so.4
#Requires:	libTD_AcisBuilder.so.1
#Requires:	libTD_Alloc.so.1
#Requires:	libTD_Br.so.1
#Requires:	libTD_BrepRenderer.so.1
#Requires:	libTD_Db.so.1
#Requires:	libTD_DbRoot.so.1
#Requires:	libTD_Dwf7Export.so.1
#Requires:	libTD_FtFontEngine.so.1
#Requires:	libTD_Ge.so.1
#Requires:	libTD_Gi.so.1
#Requires:	libTD_Gs.so.1
#Requires:	libTD_PDFToolkit.so.1
#Requires:	libTD_PdfExport.so.1
#Requires:	libTD_Root.so.1
#Requires:	libTD_SpatialIndex.so.1
#Requires:	libTD_SvgExport.so.1
#Requires:	libW3dTk.so.1
#Requires:	libWhipTk.so.1
#Requires:	libX11.so.6
#Requires:	libc.so.6
#Requires:	libc.so.6(GLIBC_2.0)
#Requires:	libc.so.6(GLIBC_2.1)
#Requires:	libc.so.6(GLIBC_2.1.2)
#Requires:	libc.so.6(GLIBC_2.1.3)
#Requires:	libc.so.6(GLIBC_2.2)
#Requires:	libc.so.6(GLIBC_2.3)
#Requires:	libc.so.6(GLIBC_2.3.2)
#Requires:	libc.so.6(GLIBC_2.3.4)
#Requires:	libc.so.6(GLIBC_2.4)
#Requires:	libcups.so.2
#Requires:	libdl.so.2
#Requires:	libdl.so.2(GLIBC_2.0)
#Requires:	libdl.so.2(GLIBC_2.1)
#Requires:	libfxsisl.so.1
#Requires:	libgcc_s.so.1
#Requires:	libgcc_s.so.1(GCC_3.0)
#Requires:	libgcc_s.so.1(GLIBC_2.0)
#Requires:	libm.so.6
#Requires:	libm.so.6(GLIBC_2.0)
#Requires:	libm.so.6(GLIBC_2.1)
#Requires:	libphonon.so.4
#Requires:	libpthread.so.0
#Requires:	libpthread.so.0(GLIBC_2.0)
#Requires:	libpthread.so.0(GLIBC_2.1)
#Requires:	libpthread.so.0(GLIBC_2.2)
#Requires:	libstdc++.so.6
#Requires:	libstdc++.so.6(CXXABI_1.3)
#Requires:	libstdc++.so.6(GLIBCXX_3.4)
#Requires:	libstdc++.so.6(GLIBCXX_3.4.11)
#Requires:	libstdc++.so.6(GLIBCXX_3.4.9)
#Requires:	libz.so.1
#Requires:	rpmlib(CompressedFileNames) <= 3.0.4-1
#Requires:	rpmlib(PayloadFilesHavePrefix) <= 4.0-1
#Requires:	rtld(GNU_HASH)
Requires:	libaudio.so.2

Provides:	lfbmp.so.18  
Provides:	lfcmp.so.18  
Provides:	lffax.so.18  
Provides:	lfgif.so.18  
Provides:	lfj2k.so.18  
Provides:	lfjb2.so.18  
Provides:	lfjbg.so.18  
Provides:	lfjls.so.18  
Provides:	lfjxr.so.18  
Provides:	lfpng.so.18  
Provides:	lfpsd.so.18  
Provides:	lftif.so.18  
Provides:	libAcDgnLS.so.1  
Provides:	libAecArchBase.so.1  
Provides:	libAecArchDACHBase.so.1  
Provides:	libAecAreaCalculationBase.so.1  
Provides:	libAecBase.so.1  
Provides:	libAecGeometry.so.1  
Provides:	libAecSchedule.so.1  
Provides:	libAecScheduleData.so.1  
Provides:	libAecStructureBase.so.1  
Provides:	libDDKERNEL.so.1  
Provides:	libDGNImport.so.1  
Provides:	libDwfCore.so.1  
Provides:	libDwfToolkit.so.1  
Provides:	libExtCommands.so.1  
Provides:	libFXCommands.so.1  
Provides:	libFXCommandsBase.so.1  
Provides:	libFXCrashRpt.so.1  
Provides:	libFXCurves.so.1  
Provides:	libFXDimCommands.so.1  
Provides:	libFXEvalWatcher.so.1  
Provides:	libFXExport.so.1  
Provides:	libFXGripPoints.so.1  
Provides:	libFXLISP.so.1  
Provides:	libFXProperties.so.1  
Provides:	libFXRenderBase.so.1  
Provides:	libFxCharMap.so.1  
Provides:	libFxDesignResources.so.1  
Provides:	libFxFileDialogs.so.1  
Provides:	libFxImages.so.1  
Provides:	libFxQtImagePlugin.so.1  
Provides:	libFxStandards.so.1  
Provides:	libGestureWidget.so.1  
Provides:	libK2AVCommand.so.1  
Provides:	libK2CrashReportSendService.so.1  
Provides:	libK2TaskPane.so.1  
Provides:	libModelerGeometry.so.1  
Provides:	libOdQtOpenGL.so.1  
Provides:	libPSToolkit.so.1  
Provides:	libPlotStyleServices.so.1  
Provides:	libQtCLucene.so.4  
Provides:	libQtCore.so.4  
Provides:	libQtDBus.so.4  
Provides:	libQtGui.so.4  
Provides:	libQtHelp.so.4  
Provides:	libQtMultimedia.so.4  
Provides:	libQtNetwork.so.4  
Provides:	libQtOpenGL.so.4  
Provides:	libQtSql.so.4  
Provides:	libQtSvg.so.4  
Provides:	libQtWebKit.so.4  
Provides:	libQtXml.so.4  
Provides:	libQtXmlPatterns.so.4  
Provides:	libRasterProcessor.so.1  
Provides:	libRecomputeDimBlock.so.1  
Provides:	libRxRasterServices.so.1  
Provides:	libTD_AcisBuilder.so.1  
Provides:	libTD_Alloc.so.1  
Provides:	libTD_Ave.so.1  
Provides:	libTD_Br.so.1  
Provides:	libTD_BrepRenderer.so.1  
Provides:	libTD_Db.so.1  
Provides:	libTD_DbRoot.so.1  
Provides:	libTD_DgnImport.so.1  
Provides:	libTD_DgnUnderlay.so.1  
Provides:	libTD_Dwf7Export.so.1  
Provides:	libTD_Dwf7Import.so.1  
Provides:	libTD_DynBlocks.so.1  
Provides:	libTD_FtFontEngine.so.1  
Provides:	libTD_Ge.so.1  
Provides:	libTD_Gi.so.1  
Provides:	libTD_Gs.so.1  
Provides:	libTD_PDFToolkit.so.1  
Provides:	libTD_PdfExport.so.1  
Provides:	libTD_Root.so.1  
Provides:	libTD_STLExport.so.1  
Provides:	libTD_SpatialIndex.so.1  
Provides:	libTD_SvgExport.so.1  
Provides:	libTG_Db.so.1  
Provides:	libTG_Dgn7IO.so.1  
Provides:	libTG_ModelerGeometry.so.1  
Provides:	libW3dTk.so.1  
Provides:	libWhipTk.so.1  
Provides:	libfreetype.so.6  
Provides:	libfxsisl.so.1  
Provides:	libltfil.so.18  
Provides:	libltkrn.so.18  
Provides:	libphonon.so.4  
Provides:	libqcncodecs.so  
Provides:	libqgif.so  
Provides:	libqico.so  
Provides:	libqjpcodecs.so  
Provides:	libqjpeg.so  
Provides:	libqkrcodecs.so  
Provides:	libqmng.so  
Provides:	libqsqlite.so  
Provides:	libqsvg.so  
Provides:	libqtiff.so  
Provides:	libqtwcodecs.so  
Provides:	draftsight = 2014.3.70-2
Provides:	draftsight(x86-32) = 2014.3.70-2

ExclusiveArch:	i686

%description
Free CAD software for your DWG files by Dassault Systèmes (standalone license).
DraftSight lets professional CAD users, students and educators create, edit and
view DWG files. DraftSight runs on Windows®, Mac® and Linux.

%prep
%setup -q -c -T


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
pushd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idV --quiet
popd

%post
cd "//opt/dassault-systemes/DraftSight/Resources" && xdg-mime install --novendor --mode system "dassault-systemes_draftsight-dwg.xml"
cd "//opt/dassault-systemes/DraftSight/Resources" && xdg-mime install --novendor --mode system "dassault-systemes_draftsight-dxf.xml"
cd "//opt/dassault-systemes/DraftSight/Resources" && xdg-mime install --novendor --mode system "dassault-systemes_draftsight-dwt.xml"

# TODO: Set mime types "application/vnd.dassault-systems.*" for all users

for SIZE in 16 32 48 64 128; do
    OPTS="--noupdate --novendor --mode system --size ${SIZE}"
    cd "//opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}"
    xdg-icon-resource install ${OPTS} --context apps "program.png" "dassault-systemes.draftsight"
    xdg-icon-resource install ${OPTS} --context apps --theme gnome "program.png" "dassault-systemes.draftsight"
    xdg-icon-resource install ${OPTS} --context mimetypes "file-dwg.png" "application-vnd.dassault-systemes.draftsight-dwg"
    xdg-icon-resource install ${OPTS} --context mimetypes --theme gnome "file-dwg.png" "application-vnd.dassault-systemes.draftsight-dwg"
    xdg-icon-resource install ${OPTS} --context mimetypes "file-dxf.png" "application-vnd.dassault-systemes.draftsight-dxf"
    xdg-icon-resource install ${OPTS} --context mimetypes --theme gnome "file-dxf.png" "application-vnd.dassault-systemes.draftsight-dxf"
    xdg-icon-resource install ${OPTS} --context mimetypes "file-dwt.png" "application-vnd.dassault-systemes.draftsight-dwt"
    xdg-icon-resource install ${OPTS} --context mimetypes --theme gnome "file-dwt.png" "application-vnd.dassault-systemes.draftsight-dwt"
done

xdg-icon-resource forceupdate
cd "//opt/dassault-systemes/DraftSight/Resources" && xdg-desktop-menu install --novendor --mode system "dassault-systemes_draftsight.desktop"
[ -x /usr/bin/update-mime-database ] && /usr/bin/update-mime-database

# prepare for dongle
if [ /etc/udev/rules.d/ ]; then
  echo "BUS==\"usb\", SYSFS{idVendor}==\"096e\", MODE==\"0666\""> /etc/udev/rules.d/ft-rockey.rules
fi
# TODO: Install libaudio.so from package. Why?

update-desktop-database &> /dev/null || :
touch --no-create /usr/share/icons/hicolor &>/dev/null || :
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet /usr/share/icons/hicolor || :
fi

%preun
xdg-mime uninstall --novendor --mode system "//opt/dassault-systemes/DraftSight/Resources/dassault-systemes_draftsight-dwg.xml"
xdg-mime uninstall --novendor --mode system "//opt/dassault-systemes/DraftSight/Resources/dassault-systemes_draftsight-dxf.xml"
xdg-mime uninstall --novendor --mode system "//opt/dassault-systemes/DraftSight/Resources/dassault-systemes_draftsight-dwt.xml"

for SIZE in 16 32 48 64 128; do
    OPTS="--noupdate --mode system --size ${SIZE}"
    xdg-icon-resource uninstall ${OPTS} --context apps "dassault-systemes.draftsight"
    xdg-icon-resource uninstall ${OPTS} --context apps --theme gnome "dassault-systemes.draftsight"
    xdg-icon-resource uninstall ${OPTS} --context mimetypes "application-vnd.dassault-systemes.draftsight-dwg"
    xdg-icon-resource uninstall ${OPTS} --context mimetypes --theme gnome "application-vnd.dassault-systemes.draftsight-dwg"
    xdg-icon-resource uninstall ${OPTS} --context mimetypes "application-vnd.dassault-systemes.draftsight-dxf"
    xdg-icon-resource uninstall ${OPTS} --context mimetypes --theme gnome "application-vnd.dassault-systemes.draftsight-dxf"
    xdg-icon-resource uninstall ${OPTS} --context mimetypes "application-vnd.dassault-systemes.draftsight-dwt"
    xdg-icon-resource uninstall ${OPTS} --context mimetypes --theme gnome "application-vnd.dassault-systemes.draftsight-dwt"
done

xdg-icon-resource forceupdate
cd "//opt/dassault-systemes/DraftSight/Resources" && xdg-desktop-menu uninstall --novendor --mode system "dassault-systemes_draftsight.desktop"
[ -x /usr/bin/update-mime-database ] && /usr/bin/update-mime-database

# remove dongle preparing
[ /etc/udev/rules.d/ ] && rm /etc/udev/rules.d/ft-rockey.rules

%postun

if [ $1 -eq 0 ] ; then
    touch --no-create /usr/share/icons/hicolor &>/dev/null
    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :

%files
/opt/dassault-systemes
/var/opt/dassault-systemes

%changelog
* Sun Jun 29 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.2.70-2.R.2
- remove the most "Requires" strings
- add dependence on libaudio.so.2
- clean up spec file

* Sun Jun 01 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.1
- initial build for Fedora
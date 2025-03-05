%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-rqt-joint-trajectory-controller
Version:        4.21.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rqt_joint_trajectory_controller package

License:        Apache License 2.0
URL:            https://control.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-rospkg
Requires:       ros-jazzy-control-msgs
Requires:       ros-jazzy-controller-manager-msgs
Requires:       ros-jazzy-python-qt-binding
Requires:       ros-jazzy-qt-gui
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-rqt-gui
Requires:       ros-jazzy-rqt-gui-py
Requires:       ros-jazzy-trajectory-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Graphical frontend for interacting with joint_trajectory_controller instances.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Mar 05 2025 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.21.0-1
- Autogenerated by Bloom

* Sun Dec 15 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.17.0-1
- Autogenerated by Bloom

* Tue Oct 08 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.15.0-1
- Autogenerated by Bloom

* Thu Sep 26 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.14.0-1
- Autogenerated by Bloom

* Tue May 14 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.8.0-1
- Autogenerated by Bloom

* Fri Apr 19 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.7.0-2
- Autogenerated by Bloom

* Fri Mar 22 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.7.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Bence Magyar <bence.magyar.robotics@gmail.com> - 4.6.0-2
- Autogenerated by Bloom


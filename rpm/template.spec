%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-joint-state-broadcaster
Version:        2.16.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS joint_state_broadcaster package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-backward-ros
Requires:       ros-humble-control-msgs
Requires:       ros-humble-controller-interface
Requires:       ros-humble-generate-parameter-library
Requires:       ros-humble-hardware-interface
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rclcpp-lifecycle
Requires:       ros-humble-rcutils
Requires:       ros-humble-realtime-tools
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-backward-ros
BuildRequires:  ros-humble-control-msgs
BuildRequires:  ros-humble-controller-interface
BuildRequires:  ros-humble-generate-parameter-library
BuildRequires:  ros-humble-hardware-interface
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rclcpp-lifecycle
BuildRequires:  ros-humble-rcutils
BuildRequires:  ros-humble-realtime-tools
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gmock
BuildRequires:  ros-humble-controller-manager
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-ros2-control-test-assets
%endif

%description
Broadcaster to publish joint state

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Jan 24 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.16.0-1
- Autogenerated by Bloom

* Thu Jan 19 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.0.0-1
- Autogenerated by Bloom

* Tue Dec 06 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.15.0-1
- Autogenerated by Bloom

* Fri Nov 18 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.14.0-1
- Autogenerated by Bloom

* Wed Oct 05 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.13.0-1
- Autogenerated by Bloom

* Thu Sep 01 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.0-1
- Autogenerated by Bloom

* Thu Aug 04 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.11.0-1
- Autogenerated by Bloom

* Mon Aug 01 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.10.0-1
- Autogenerated by Bloom

* Thu Jul 14 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.9.0-1
- Autogenerated by Bloom

* Sat Jul 09 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.8.0-1
- Autogenerated by Bloom

* Sun Jul 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.7.0-1
- Autogenerated by Bloom

* Sat Jun 18 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.6.0-1
- Autogenerated by Bloom

* Thu May 19 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.5.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.2.0-2
- Autogenerated by Bloom

* Fri Mar 25 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.2.0-1
- Autogenerated by Bloom

* Wed Feb 23 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.1.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.0.1-2
- Autogenerated by Bloom


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-vishvananda-netlink
Version  : a632d6dc2806fa19d2f7693017d3fb79d3d8fa03
Release  : 4
URL      : https://github.com/vishvananda/netlink/archive/a632d6dc2806fa19d2f7693017d3fb79d3d8fa03.tar.gz
Source0  : https://github.com/vishvananda/netlink/archive/a632d6dc2806fa19d2f7693017d3fb79d3d8fa03.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go

%description
# netlink - netlink library for go #
[![Build Status](https://travis-ci.org/vishvananda/netlink.png?branch=master)](https://travis-ci.org/vishvananda/netlink) [![GoDoc](https://godoc.org/github.com/vishvananda/netlink?status.svg)](https://godoc.org/github.com/vishvananda/netlink)

%prep
%setup -q -n netlink-a632d6dc2806fa19d2f7693017d3fb79d3d8fa03

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/vishvananda/netlink"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/vishvananda/netlink/addr.go
/usr/lib/golang/src/github.com/vishvananda/netlink/addr_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/addr_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/bpf_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/class.go
/usr/lib/golang/src/github.com/vishvananda/netlink/class_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/class_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/filter.go
/usr/lib/golang/src/github.com/vishvananda/netlink/filter_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/filter_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/link.go
/usr/lib/golang/src/github.com/vishvananda/netlink/link_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/link_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/link_tuntap_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/neigh.go
/usr/lib/golang/src/github.com/vishvananda/netlink/neigh_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/neigh_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/netlink.go
/usr/lib/golang/src/github.com/vishvananda/netlink/netlink_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/netlink_unspecified.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/addr_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/addr_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/link_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/link_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/nl_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/nl_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/route_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/route_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/syscall.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/tc_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/tc_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/xfrm_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/xfrm_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/xfrm_policy_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/xfrm_policy_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/xfrm_state_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/nl/xfrm_state_linux_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/protinfo.go
/usr/lib/golang/src/github.com/vishvananda/netlink/protinfo_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/protinfo_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/qdisc.go
/usr/lib/golang/src/github.com/vishvananda/netlink/qdisc_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/qdisc_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/route.go
/usr/lib/golang/src/github.com/vishvananda/netlink/route_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/route_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/rule.go
/usr/lib/golang/src/github.com/vishvananda/netlink/rule_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/rule_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/xfrm.go
/usr/lib/golang/src/github.com/vishvananda/netlink/xfrm_policy.go
/usr/lib/golang/src/github.com/vishvananda/netlink/xfrm_policy_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/xfrm_policy_test.go
/usr/lib/golang/src/github.com/vishvananda/netlink/xfrm_state.go
/usr/lib/golang/src/github.com/vishvananda/netlink/xfrm_state_linux.go
/usr/lib/golang/src/github.com/vishvananda/netlink/xfrm_state_test.go

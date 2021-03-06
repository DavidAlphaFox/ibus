# vim:set noet ts=4:
#
# ibus - The Input Bus
#
# Copyright (c) 2007-2015 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2015-2018 Takao Fujiwara <takao.fujiwara1@gmail.com>
# Copyright (c) 2007-2017 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

NULL =

if ENABLE_TESTS
TESTS_DIR = tests
endif

SUBDIRS = . $(TESTS_DIR)

# libibus = libibus-@IBUS_API_VERSION@.la
libibus = libibus-1.0.la

# gobject introspection
-include $(INTROSPECTION_MAKEFILE)
INTROSPECTION_SCANNER_ARGS =
INTROSPECTION_COMPILER_ARGS = \
    --includedir=$(srcdir)    \
    --includedir=.            \
    $(NULL)
INTROSPECTION_GIRS =
CLEANFILES =
noinst_PROGRAMS =

# C preprocessor flags
AM_CPPFLAGS =                                           \
    -DG_LOG_DOMAIN=\"IBUS\"                             \
    @GLIB2_CFLAGS@                                      \
    @GOBJECT2_CFLAGS@                                   \
    @GIO2_CFLAGS@                                       \
    -DIBUS_CACHE_DIR=\""$(localstatedir)/cache/ibus"\"  \
    -DIBUS_DATA_DIR=\"$(pkgdatadir)\"                   \
    -DIBUS_DISABLE_DEPRECATION_WARNINGS                 \
    -DIBUS_COMPILATION                                  \
    -DISOCODES_PREFIX=\"$(ISOCODES_PREFIX)\"            \
    -DX11_DATA_PREFIX=\"$(X11_PREFIX)\"                 \
    $(NULL)

# ibus library
lib_LTLIBRARIES = $(libibus)

libibus_1_0_la_LIBADD =     \
    @GLIB2_LIBS@            \
    @GOBJECT2_LIBS@         \
    @GIO2_LIBS@             \
    $(NULL)
libibus_1_0_la_LDFLAGS =            \
    -no-undefined                   \
    -export-symbols-regex "ibus_.*" \
    -version-info @LT_VERSION_INFO@ \
    $(NULL)

ibus_sources =              \
    ibusaccelgroup.c        \
    ibusattribute.c         \
    ibusattrlist.c          \
    ibusbus.c               \
    ibuscomponent.c         \
    ibusconfig.c            \
    ibusconfigservice.c     \
    ibusemoji.c             \
    ibusengine.c            \
    ibusenginedesc.c        \
    ibusenginesimple.c      \
    ibuserror.c             \
    ibusfactory.c           \
    ibushotkey.c            \
    ibusinputcontext.c      \
    ibuskeymap.c            \
    ibuskeynames.c          \
    ibuskeyuni.c            \
    ibuslookuptable.c       \
    ibusobject.c            \
    ibusobservedpath.c      \
    ibuspanelservice.c      \
    ibusproperty.c          \
    ibusproplist.c          \
    ibusproxy.c             \
    ibusregistry.c          \
    ibusserializable.c      \
    ibusservice.c           \
    ibusshare.c             \
    ibustext.c              \
    ibusunicode.c           \
    ibusutil.c              \
    ibusxevent.c            \
    ibusxml.c               \
    $(NULL)
libibus_1_0_la_SOURCES =    \
    ibuscomposetable.c      \
    ibusenumtypes.c         \
    ibusmarshalers.c        \
    $(ibus_sources)         \
    $(NULL)
ibus_marshalers_sources =   \
    ibusmarshalers.c        \
    ibusmarshalers.h        \
    $(NULL)
ibus_enumtypes_sources =    \
    ibusenumtypes.c         \
    ibusenumtypes.h         \
    $(NULL)
ibus_headers =              \
    ibus.h                  \
    ibusaccelgroup.h        \
    ibusattribute.h         \
    ibusattrlist.h          \
    ibusbus.h               \
    ibuscomponent.h         \
    ibusconfig.h            \
    ibusconfigservice.h     \
    ibusdebug.h             \
    ibusemoji.h             \
    ibusengine.h            \
    ibusenginedesc.h        \
    ibusenginesimple.h      \
    ibuserror.h             \
    ibusfactory.h           \
    ibushotkey.h            \
    ibusinputcontext.h      \
    ibuskeymap.h            \
    ibuskeys.h              \
    ibuskeysyms-compat.h    \
    ibuskeysyms.h           \
    ibuslookuptable.h       \
    ibusobject.h            \
    ibusobservedpath.h      \
    ibuspanelservice.h      \
    ibusproperty.h          \
    ibusproplist.h          \
    ibusproxy.h             \
    ibusregistry.h          \
    ibusserializable.h      \
    ibusservice.h           \
    ibusshare.h             \
    ibustext.h              \
    ibustypes.h             \
    ibusunicode.h           \
    ibusutil.h              \
    ibusxevent.h            \
    ibusxml.h               \
    $(NULL)
ibusincludedir = $(includedir)/ibus-@IBUS_API_VERSION@
ibus_public_headers =       \
    $(ibus_headers)         \
    ibusenumtypes.h         \
    ibusversion.h           \
    $(NULL)
ibusinclude_HEADERS =       \
    $(ibus_public_headers)  \
    $(NULL)
ibus_private_headers =          \
    gtkimcontextsimpleseqs.h    \
    ibuscomposetable.h          \
    ibusemojigen.h              \
    ibusenginesimpleprivate.h   \
    ibusinternal.h              \
    ibusunicodegen.h            \
    keyname-table.h             \
    $(NULL)
noinst_HEADERS =            \
    $(ibus_private_headers) \
    $(NULL)

BUILT_SOURCES =                 \
    $(ibus_marshalers_sources)  \
    $(ibus_enumtypes_sources)   \
    $(NULL)

if HAVE_INTROSPECTION
introspection_sources =         \
    $(ibus_headers)             \
    $(ibus_sources)             \
    $(NULL)
built_introspection_sources =   \
    $(ibus_enumtypes_sources)   \
    ibusversion.h               \
    $(NULL)
IBus-1.0.gir: $(libibus) Makefile
IBus_1_0_gir_SCANNERFLAGS = --pkg-export=ibus-1.0 $(IBUS_GIR_SCANNERFLAGS)
IBus_1_0_gir_INCLUDES = GLib-2.0 GObject-2.0 Gio-2.0
IBus_1_0_gir_LIBS = $(libibus)
IBus_1_0_gir_FILES =                                            \
    $(addprefix $(srcdir)/,$(introspection_sources))            \
    $(addprefix $(builddir)/,$(built_introspection_sources))    \
    $(NULL)
IBus_1_0_gir_CFLAGS = -DIBUS_COMPILATION -I$(srcdir) -I$(builddir)
INTROSPECTION_GIRS += IBus-1.0.gir

girdir = $(datadir)/gir-1.0
dist_gir_DATA = $(INTROSPECTION_GIRS)

typelibsdir = $(libdir)/girepository-1.0
typelibs_DATA = $(INTROSPECTION_GIRS:.gir=.typelib)

CLEANFILES += $(dist_gir_DATA) $(typelibs_DATA)
endif

# gen enum types
ibusenumtypes.h: $(ibus_headers) ibusenumtypes.h.template
	$(AM_V_GEN) ( top_builddir=`cd $(top_builddir) && pwd`; \
	cd $(srcdir) && $(GLIB_MKENUMS) --template ibusenumtypes.h.template $(ibus_headers) | \
		sed 's/i_bus_/ibus_/g' | \
		sed 's/I_TYPE_BUS_/IBUS_TYPE_/g') > \
	ibusenumtypes.h.tmp && mv ibusenumtypes.h.tmp ibusenumtypes.h

ibusenumtypes.c: $(ibus_headers) ibusenumtypes.c.template
	$(AM_V_GEN) ( top_builddir=`cd $(top_builddir) && pwd`; \
	cd $(srcdir) && $(GLIB_MKENUMS) --template ibusenumtypes.c.template $(ibus_headers) | \
		sed 's/i_bus_/ibus_/g' | \
		sed 's/I_TYPE_BUS_/IBUS_TYPE_/g') > \
	ibusenumtypes.c.tmp && mv ibusenumtypes.c.tmp ibusenumtypes.c

# gen marshal
ibusmarshalers.h: ibusmarshalers.list
	$(AM_V_GEN) $(GLIB_GENMARSHAL) --prefix=_ibus_marshal $(srcdir)/ibusmarshalers.list --header --internal > $@.tmp && \
	mv $@.tmp $@

ibusmarshalers.c: ibusmarshalers.h ibusmarshalers.list
	$(AM_V_GEN) (echo "#include \"ibusmarshalers.h\""; \
	$(GLIB_GENMARSHAL) --prefix=_ibus_marshal $(srcdir)/ibusmarshalers.list --body --internal) > $@.tmp && \
	mv $@.tmp $@

if ENABLE_EMOJI_DICT
AM_CPPFLAGS += -DENABLE_EMOJI_DICT

dictdir = $(pkgdatadir)/dicts
dict_DATA = dicts/emoji-en.dict
LANG_FILES = $(basename $(notdir $(wildcard $(EMOJI_ANNOTATION_DIR)/*.xml)))

noinst_PROGRAMS += emoji-parser

dicts/emoji-en.dict: emoji-parser
	$(AM_V_at)if test x"$(LANG_FILES)" = x ; then \
	    echo "WARNING: Not found $(EMOJI_ANNOTATION_DIR)/en.xml" 1>&2; \
	fi; \
	for f in $(LANG_FILES) ; do \
	    if test -f \
	    "$(EMOJI_ANNOTATION_DIR)/../annotationsDerived/$$f.xml" ; then \
	        xml_derived_option="--xml-derived $(EMOJI_ANNOTATION_DIR)/../annotationsDerived/$$f.xml"; \
	        plus_comment="derived"; \
	    fi; \
	    if test x"$$f" = xen ; then \
	        $(builddir)/emoji-parser \
	            --unicode-emoji-dir $(UNICODE_EMOJI_DIR) \
	            --xml $(EMOJI_ANNOTATION_DIR)/$$f.xml \
	            $$xml_derived_option \
	            --xml-ascii $(top_srcdir)/data/annotations/en_ascii.xml \
	            --out-category ibusemojigen.h \
	            --out $@; \
	    else \
	        $(builddir)/emoji-parser \
	            --unicode-emoji-dir $(UNICODE_EMOJI_DIR) \
	            --xml $(EMOJI_ANNOTATION_DIR)/$$f.xml \
	            $$xml_derived_option \
	            --out dicts/emoji-$$f.dict; \
	    fi; \
	    echo "Generated $$plus_comment dicts/emoji-$$f.dict"; \
	done

install-data-hook: $(dict_DATA)
	@$(NORMAL_INSTALL)
	$(AM_V_at)list='$(wildcard dicts/*.dict)'; \
        test -n "$(dictdir)" || list=; \
	if test -n "$$list"; then \
	  echo " $(MKDIR_P) '$(DESTDIR)$(dictdir)'"; \
	  $(MKDIR_P) "$(DESTDIR)$(dictdir)" || exit 1; \
	fi; \
	for p in $$list; do \
	  if test -f "$$p"; then d=; else d="$(srcdir)/"; fi; \
	  echo "$$d$$p"; \
	done | \
	while read files; do \
	  if [ x$(AM_DEFAULT_VERBOSITY) = x1 ] ; then \
	      echo "$(INSTALL_DATA) $$files '$(DESTDIR)$(dictdir)'"; \
	  else \
	      echo "Installing $$files"; \
	  fi; \
	  $(INSTALL_DATA) $$files "$(DESTDIR)$(dictdir)" || exit $$?; \
	done

dict__uninstall_files_from_dir = { \
    test -z "$$files" \
        || { test ! -d "$$dir" && test ! -f "$$dir" && test ! -r "$$dir"; } \
        || { echo " ( cd '$$dir' && rm -f" $$files ")"; \
             cd "$$dir" && rm -f $$files; }; \
    }

# for make dist
uninstall-hook:
	@$(NORMAL_UNINSTALL)
	$(AM_V_at)list='$(wildcard dicts/*.dict)'; \
	test -n "$(dictdir)" || list=; \
	files=`for p in $$list; do echo $$p; done | sed -e 's|^.*/||'`; \
	dir='$(DESTDIR)$(dictdir)'; $(dict__uninstall_files_from_dir)

emoji_parser_SOURCES =          \
    emoji-parser.c              \
    $(NULL)
emoji_parser_CFLAGS =           \
    $(GLIB2_CFLAGS)             \
    $(GOBJECT2_CFLAGS)          \
    $(NULL)
emoji_parser_LDADD =            \
    $(libibus)                  \
    $(GLIB2_LIBS)               \
    $(GOBJECT2_LIBS)            \
    $(NULL)

clean-local:
	-rm -rf dicts
	$(NULL)
endif

if ENABLE_UNICODE_DICT
unicodedir = $(pkgdatadir)/dicts
unicode_DATA = dicts/unicode-names.dict dicts/unicode-blocks.dict
noinst_PROGRAMS += unicode-parser

dicts/unicode-names.dict: unicode-parser
	$(AM_V_at)input_file="$(UCD_DIR)/NamesList.txt"; \
	if test ! -f "$$input_file" ; then \
	    echo "WARNING: Not found $$input_file" 1>&2; \
	else \
	    $(builddir)/unicode-parser \
	        --input-names-list $$input_file \
	        --output-names-list $@; \
	    echo "Generated $@"; \
	fi;

dicts/unicode-blocks.dict: unicode-parser
	$(AM_V_at)input_file="$(UCD_DIR)/Blocks.txt"; \
	if test ! -f "$$input_file" ; then \
	    echo "WARNING: Not found $$input_file" 1>&2; \
	else \
	    $(builddir)/unicode-parser \
	        --input-blocks $$input_file \
	        --output-blocks-trans ibusunicodegen.h \
	        --output-blocks $@; \
	    echo "Generated $@"; \
	fi;

ibusunicodegen.h: dicts/unicode-blocks.dict
	$(NULL)

unicode_parser_SOURCES =        \
    unicode-parser.c            \
    $(NULL)
unicode_parser_CFLAGS =         \
    $(GLIB2_CFLAGS)             \
    $(NULL)
unicode_parser_LDADD =          \
    $(GLIB2_LIBS)               \
    $(libibus)                  \
    $(NULL)

clean-local:
	-rm -rf dicts
	$(NULL)
endif

EXTRA_DIST =                    \
    emoji-parser.c              \
    ibusversion.h.in            \
    ibusmarshalers.list         \
    ibusenumtypes.h.template    \
    ibusenumtypes.c.template    \
    unicode-parser.c            \
    $(NULL)

CLEANFILES +=                   \
    $(BUILT_SOURCES)            \
    stamp-ibusmarshalers.h      \
    stamp-ibusenumtypes.h       \
    $(NULL)

DISTCLEANFILES =                \
    ibusemojigen.h              \
    ibusunicodegen.h            \
    ibusversion.h               \
    $(NULL)

-include $(top_srcdir)/git.mk

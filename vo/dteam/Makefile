DATE=20110325

VO=dteam
LSCFILES=voms2.hellasgrid.gr.lsc voms.hellasgrid.gr.lsc
FILES=$(VO) ChangeLog README $(LSCFILES) voms-conf-$(VO).spec Makefile LICENSE


install: 
	mkdir -p $(DESTDIR)/etc/vomses
	mkdir -p $(DESTDIR)/etc/grid-security/vomsdir
	install -p -m 644 $(VO) $(DESTDIR)/etc/vomses/.
	install -p -m 644 $(LSCFILES) $(DESTDIR)/etc/grid-security/vomsdir/.

clean: 
	rm -rf voms-conf-$(VO)-$(DATE)
	rm -f voms-conf-$(VO)-$(DATE).tar.gz

sources: clean $(FILES)
	mkdir voms-conf-$(VO)-$(DATE)
	cp $(FILES) voms-conf-$(VO)-$(DATE)
	tar cvfz voms-conf-$(VO)-$(DATE).tar.gz voms-conf-$(VO)-$(DATE)

rpm: sources
	rpmbuild -ba --define "_sourcedir ${PWD}" voms-conf-$(VO).spec


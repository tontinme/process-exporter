## build rpm

下载process-exporter bin文件tar包,拷贝二进制文件process-exporter到process-exporter-0.3.10/

```
tar zcvf process-exporter-0.3.10.tar.gz process-exporter-0.3.10/
cp process-exporter-0.3.10.tar.gz SOURCES/
cp process_exporter.spec SPECS/
cd rpmbuild/
rpmbuild -ba SPECS/process_exporter.spec
```

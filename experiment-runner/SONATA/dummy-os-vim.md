+ Record tcpdump
    - https://askubuntu.com/questions/252179/how-to-inspect-outgoing-http-requests-of-a-single-application

+ tcpdump - examples
    - https://danielmiessler.com/study/tcpdump/


sudo tcpdump -i any -w /tmp/http.log &
killall tcpdump

sudo tcpdump -A dst 131.234.250.117 -r /tmp/http.log > OS.logs

---

sudo tcpdump -i any dst 131.234.250.117 -w /tmp/os2.log &

---

# To gernerate HTTPolice report

sudo tcpflow -T'%t-%A-%a-%B-%b-%#' -i ens160 host 131.234.250.117

httpolice -i tcpflow -o html . >../report.html
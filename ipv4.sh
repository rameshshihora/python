for i in `cat 1 `
do
    llama ipam get-cidr-parent $i > temp.out
    NAME=$i
    CIDR=$(grep CIDR temp.out | awk '{ print $(NF-1) }')
    VLAN=$(grep VLAN temp.out | awk '{ print $(NF-1) }'| awk '{ print "_Vlan"$1 }')
    SITE=$(grep Site temp.out | awk '{ print $(NF-1) }'|tr -s 'A-Z' 'a-z')
    Vname=$(echo "$SITE$VLAN")

    echo "$NAME,$CIDR,$SITE$VLAN"
done

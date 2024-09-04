import pydivert

def main():
       # Define a filter to capture traffic on multiple common ports
    filters_to_intercept = (
        "tcp.DstPort == 443 or tcp.SrcPort == 443 or "
        "tcp.DstPort == 80 or tcp.SrcPort == 80 or "
        "tcp.DstPort == 21 or tcp.SrcPort == 21 or "
        "tcp.DstPort == 53 or tcp.SrcPort == 53 or "
        "tcp.DstPort == 22 or tcp.SrcPort == 22 or "
        "tcp.DstPort == 110 or tcp.SrcPort == 110 or "
        "tcp.DstPort == 143 or tcp.SrcPort == 143"
    )
    with pydivert.WinDivert(filters_to_intercept) as w:
        print("Interception is taking place")

        # Loop through each packet captured
        for packet in w:
            # Log details about the packet based onport 80 (HTTP)
            if packet.dst_port == 80 or packet.src_port ==80:
                _extracted_from_main_11(packet)
            elif packet.dst_port == 443 or packet.src_port == 443:
                _extracted_from_main_11(packet)
            elif packet.dst_port == 21 or packet.src_port == 21:
                _extracted_from_main_11(packet)
            elif packet.dst_port == 53 or packet.src_port == 53:
                _extracted_from_main_11(packet)
            elif packet.dst_port == 22 or packet.src_port == 22:
                _extracted_from_main_11(packet)
            elif packet.dst_port == 110 or packet.src_port == 110:
                _extracted_from_main_11(packet)
            elif packet.dst_port == 143 or packet.src_port == 143:
                _extracted_from_main_11(packet)
            # Reinject the packet into the network
            w.send(packet)


# TODO Rename this here and in `main`
def _extracted_from_main_11(packet):
    print(f"Source IP: {packet.src_addr}")
    print(f"Destination IP: {packet.dst_addr}")
    print(f"Source Port: {packet.src_port}")
    print(f"Destination Port: {packet.dst_port}")

if __name__ == "__main__":
    main()

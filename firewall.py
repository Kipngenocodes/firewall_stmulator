import pydivert

def main():
    # Intercepting TCP packets on port 80 (HTTP)
    with pydivert.WinDivert("tcp.DstPort == 443 or tcp.SrcPort == 443") as w:
        print("Interception is taking place")
        
        # Loop through each packet captured
        for packet in w:
            # Log details about the packet
            print(f"Source IP: {packet.src_addr}")
            print(f"Destination IP: {packet.dst_addr}")
            print(f"Source Port: {packet.src_port}")
            print(f"Destination Port: {packet.dst_port}")
            
            # Reinject the packet into the network
            w.send(packet)

if __name__ == "__main__":
    main()

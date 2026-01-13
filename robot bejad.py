import heapq
import matplotlib.pyplot as plt
import networkx as nx


graph = {
    "MJS": {"MJK": 14, "SDA": 28},
    "MJK": {"MJS": 14, "KR": 20, "SDA": 15},
    "KR": {"MJK": 20, "SBY": 28, "SDA": 15},
    "SDA": {"MJS": 28, "MJK": 15, "KR": 15, "SBY": 25},
    "SBY": {"KR": 28, "SDA": 25},
    "KUI": {"KR": 28, "SDA": 25,"MJS": 40}
}

def dijkstra(graph, start):
    """Algoritma Dijkstra untuk mencari jarak terpendek dari start ke semua node"""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph.get(current, {}).items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous

def get_path(previous, start, end):
    """Rekonstruksi jalur dari previous"""
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]
    return path[::-1]

def hitung_semua_jarak():
    """Hitung jarak terpendek dari semua kota ke semua kota"""
    all_distances = {}
    all_previous = {}
    
    for node in graph:
        distances, previous = dijkstra(graph, node)
        all_distances[node] = distances
        all_previous[node] = previous
    
    return all_distances, all_previous

def tampilkan_menu():
    print("\n=== SISTEM PENCARIAN RUTE TERPENDEK ===")
    print("1. Lihat semua jarak antar kota")
    print("2. Cari rute terpendek")
    print("3. Visualisasi graf")
    print("4. Keluar")
    return input("Pilih menu (1-4): ")

def visualisasi_graf(jalur_terpendek=None):
    """Visualisasi graf dengan matplotlib dan networkx"""
    G = nx.Graph()
    
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
   
    pos = {
        'MJS': (0, 2),      # A - kiri
        'MJK': (2, 3),      # B - atas tengah
        'KR': (4, 3),       # C - kanan atas
        'SDA': (2, 0),      # E - bawah tengah
        'SBY': (5, 1.5),     # D - kanan
        'KUI': (5, 6)
    }
    
    plt.figure(figsize=(12, 8))
    
    # Gambar semua edges dengan warna abu-abu
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.3, edge_color='gray')
    
    # Tambahkan label jarak pada edges
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    
    # Highlight jalur terpendek jika ada
    total_distance = 0
    if jalur_terpendek and len(jalur_terpendek) > 1:
        jalur_edges = [(jalur_terpendek[i], jalur_terpendek[i+1]) 
                       for i in range(len(jalur_terpendek)-1)]
        
        # Hitung total jarak
        for i in range(len(jalur_terpendek)-1):
            total_distance += graph[jalur_terpendek[i]][jalur_terpendek[i+1]]
            
        # Gambar jalur terpendek dengan warna merah
        nx.draw_networkx_edges(G, pos, edgelist=jalur_edges, 
                              width=4, edge_color='red', alpha=0.8)
        
        # Tambahkan text total jarak
        plt.text(0.02, 0.98, f'Total Jarak: {int(total_distance)} km', 
                transform=plt.gca().transAxes, 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'),
                fontsize=10)
    
    # Gambar nodes
    node_colors = []
    for node in G.nodes():
        if jalur_terpendek:
            if node == jalur_terpendek[0]:
                node_colors.append('lightgreen')  # Start
            elif node == jalur_terpendek[-1]:
                node_colors.append('blue')  # End
            elif node in jalur_terpendek:
                node_colors.append('yellow')      # Path
            else:
                node_colors.append('lightblue')
        else:
            node_colors.append('lightblue')
    
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                          node_size=2000, alpha=0.9)
    
    # Label nodes dengan nama kota
    labels = {
        'MJS': 'MJS\n(A)',
        'MJK': 'MJK\n(B)',
        'KR': 'KR\n(C)',
        'SDA': 'SDA\n(E)',
        'SBY': 'SBY\n(D)',
        'KUI': 'KUI\n(F)'
    }
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')
    
    # Label edges dengan jarak
    edge_labels = nx.get_edge_attributes(G, 'weight')
    edge_labels = {k: f"{v} km" for k, v in edge_labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=9)
    
    plt.title("Graf Jaringan Kota Jawa Timur", fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def tampilkan_tabel(all_distances):
    """Tampilkan tabel jarak terpendek"""
    nodes = list(all_distances.keys())
    
    print("\nTabel Jarak Terpendek Antar Kota:")
    header = "| Dari \\ Ke | " + " | ".join(nodes) + " |"
    print(header)
    print("|" + "-" * (len(header) - 2) + "|")
    
    for start in nodes:
        row = f"| {start:<4}|"
        for end in nodes:
            jarak = all_distances[start][end]
            if jarak == float('inf'):
                row += f" {'∞':>3}|"
            else:
                row += f" {int(jarak):>3}|"
        print(row)

def main():
    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == "1":
            # Lihat semua jarak
            all_distances, _ = hitung_semua_jarak()
            print("\nTabel Jarak Antar Kota:")
            tampilkan_tabel(all_distances)
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == "2":
            # Cari rute terpendek
            print("\nKota tersedia:", ", ".join(graph.keys()))
            asal = input("Masukkan kota asal: ").strip().upper()
            tujuan = input("Masukkan kota tujuan: ").strip().upper()
            
            if asal not in graph or tujuan not in graph:
                print("\nKota tidak ditemukan dalam data.")
            else:
                all_distances, all_previous = hitung_semua_jarak()
                jarak = all_distances[asal][tujuan]
                
                if jarak == float('inf'):
                    print(f"\nTidak ada jalur dari {asal} ke {tujuan}")
                else:
                    print(f"\nJarak terpendek dari {asal} ke {tujuan} adalah {int(jarak)}")
                    jalur = get_path(all_previous[asal], asal, tujuan)
                    print(f"Jalur: {' -> '.join(jalur)}")
                    
                    print("\nDetail perjalanan:")
                    total = 0
                    for i in range(len(jalur) - 1):
                        dari = jalur[i]
                        ke = jalur[i + 1]
                        jarak_segmen = graph[dari][ke]
                        total += jarak_segmen
                        print(f"  {dari} -> {ke}: {jarak_segmen} km")
                    print(f"Total: {total} km")
                    
                    # Visualisasi dengan jalur terpendek
                    print("\nMenampilkan visualisasi jalur terpendek...")
                    visualisasi_graf(jalur)
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == "3":
            # Visualisasi graf
            print("\nMenampilkan visualisasi graf...")
            visualisasi_graf()
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan aplikasi ini!")
            break
            
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            print(f"\nMenampilkan visualisasi jalur terpendek dari {asal} ke {tujuan}...")
            visualisasi_graf(jalur)

if __name__ == "__main__":
    main()
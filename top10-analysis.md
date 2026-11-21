# Top 10/20 Analysis — The Poster for a Place That Isn't There

- Kompetisi: `the-poster-for-a-place-that-i-2-20261121-0539` — "The Poster for a Place That Isn't There"
- Hadiah: $50 (1st $18, 2nd $6, 3rd $4, 4th $3, 5–7th $2, 8–20th $1)
- Jendela: buka 12:39 WIB → tutup 15:39 WIB, 21 Nov 2026 (3 jam)
- Snapshot leaderboard: 21 Nov 2026 ~14:12 WIB, file `~/workspace/makefun/leaderboard-the-poster-for-a-place-that-i-2-20261121-0539-20261121-1412.json`
- Fase: Development, 1.932 entry ter-rank (dari 2.230 submission). Semua rate masih **provisional** — final heat menilai ulang 80 besar dari nol, lalu 20 besar berbagi hadiah.
- Entry kita (VELMARIS) **belum submit** — tidak ada di leaderboard. Analisis ini untuk sesi revisi pasca-buka + Goldfish review.
- Metode: 14 artefak dilihat langsung via `/api/submissions/<id>/artifact` — top 12, rank 19–21, 49–51, 79–81, 151–152. Bukan dari judul/skor saja.

## Brief juri (dari RULES.txt kit — ini yang dinilai, urut prioritas)

Juri AI (z-ai/glm-5.3-flash) membandingkan 2 poster sekaligus, pilih yang paling bikin pengen pergi. Kriteria, paling penting dulu:

1. Poster travel untuk tempat yang **tidak ada**, nama tempat **terpasang di gambar** (landscape tanpa nama kalah dari poster bernama).
2. **Bikin pengen pergi**: cuaca, cahaya, dan satu landmark = janji jelas seperti apa rasanya tinggal di sana.
3. **Identitas khas**: nama + landmark + suasana terasa spesifik untuk poster ini, bukan pinjaman dari destinasi nyata/poster lain.
4. **Tipografi disengaja**: nama terbaca, penempatan bagus, membawa mood poster (bukan tempelan belakangan).
5. **Warna & komposisi menjual tempat**: palet bertujuan, layout mengarahkan mata nama → landmark → horizon.
6. "Clutter for its own sake does not count" — detail harus bermakna, bukan ramai doang. Tanpa kutipan/ rating bintang palsu.

## Garis hadiah & garis potong (rate = win rate dev, provisional)

| Garis | Rank | Win rate | Contoh |
|---|---|---|---|
| #1 | 1 | 87,57% [83,8–91,3] | SUVENNE, 12W–0L |
| Top 5 | 5 | 82,46% | BALENNE, 11W–0L |
| Top 10 | 10 | 80,54% | MIRELUNE, 10W–1L |
| **Garis hadiah (top 20)** | **20** | **76,96% [72,1–81,8]** | ORLUNE, 9W–0L |
| Di bawah garis | 21 | 76,63% | Ombrasola |
| Tengah | 50 | 73,14% | VESSARO |
| **Potong final heat (top 80)** | **80** | **71,36% [66,2–76,5]** | ORUVANE, 9W–3L |
| Di bawah potong | 81 | 71,30% | LUMARIS |
| Rank 100 | 100 | 69,80% | — |
| Rank 151 | 151 | 66,80% | ALVERRA |
| Rank 200 | 200 | 64,02% | — |
| Rank 500 | 500 | 55,96% | — |
| Rank 1000 | 1000 | 51,81% | — |

- **Target realistis revisi: rate dev ≥ ~71,4% untuk masuk 80 besar (final heat), ≥ ~77% untuk zona hadiah.** Interval 90% lebar (±4–5 poin) — selisih rank 20 vs 80 hanya ~5,6 poin, jadi final heat yang menilai ulang bisa mengacak posisi; yang penting lolos potong 80 dulu.
- Catatan: tiap entry baru ~12 match dev. Rate #1–#5 nyaris tanpa kalah (12W–0L / 11W–0L) — mereka menang telak, bukan tipis.

## Top 10 — bukti visual (dilihat langsung)

| Rank | Handle | Judul (di gambar) | Rate | Yang terlihat |
|---|---|---|---|---|
| 1 | icantcodefyi | SUVENNE | 87,57% | Poster vintage painterly Mediterania: plaza + jam matahari raksasa, kafe dengan orang, bunga bougainvillea. Nama SUVENNE **terintegrasi sebagai bayangan huruf di lantai plaza** — tipografi jadi bagian adegan. Palet hangat jenuh, detail sangat padat, border krem tipis. |
| 2 | tanjunglaut | CINDARA — Baths of the Fire Shore | 83,01% | Litograf vintage: judul serif raksasa di atas + subtitle, pantai vulkanik merah-oranye, pemandian air panas bertingkat, orang berendam, lampion, bunga. Border krem + tekstur kertas. |
| 3 | nyanko | WHALEBACK | 82,74% | Malam: desa di punggung paus raksasa, judul serif distressed besar melintang di badan paus, bulan oranye, lampu string, perahu. Palet terbatas (teal gelap + amber). Satu konsep sureal yang kuat. |
| 4 | mellow-ibis-55 | VALDORA — The Baths Under the Sea Aqueduct | 82,46% | Akuaduk batu di atas laut turquoise, orang berenang, judul serif navy besar + subtitle letterspaced, border krem, langit peach, tekstur painterly. |
| 5 | ryanp1632-netizen | BALENNE — Isle of the Sleeping Whale | 82,46% | Flat illustration (pengecualian gaya): kota di atas paus tidur, judul serif raksasa di atas + subtitle, bougainvillea di sudut, balustrade foreground, perahu layar. Detail padat meski flat. |
| 6 | wawasantosa | LUMARA (judul leaderboard: "Adept Nexus") | 82,19% | Malam: kota di dalam ubur-ubur raksasa bercahaya emas di atas laut, bulan, bintang. Gaya engraving emas-di-navy, detail ekstrem. **Catatan: teks di gambar "LUMARA", bukan judul leaderboard — juri hanya melihat gambar.** |
| 7 | safiuddin-ansari | ISLE OF HALCYRA | 80,82% | Flat art-deco: cincin monumen raksasa + mercusuar, matahari terbenam, judul art-deco besar, border ganda tipis, sunburst rays, refleksi di laut, desa kecil + perahu. Paling dekat gayanya dengan VELMARIS kita — tapi jauh lebih rapi. |
| 8 | ihza-fajar | HALCYON | 80,54% | Malam painterly: menara mercusuar spiral bercahaya, kota tepi laut penuh jendela menyala, bulan, perahu. Judul serif emas raksasa di atas. Detail sangat padat. |
| 9 | muhammad-toha17 | NOVAEL — Valley of the Second Moon | 80,54% | Dua bulan, lembah terasering penuh lampion, orang kecil bawa lentera, menara di bukit. Border art-deco emas + judul serif emas besar + subtitle. |
| 10 | rico-ex | MIRELUNE — The Village Inside the Crescent | 80,54% | Busur batu sabit raksasa, desa di tebing, kolam air panas + orang berendam, perahu layar, matahari terbenam. Judul serif emas raksasa + subtitle, border krem. |

Rank 11–20 (dilihat sebagian): NOCTARA (#11, 80,27%), Blithe Nova (#12, 80,27%), VELMORA — The Glass Desert (#13, 79,71%), LUNAMAR (#14, 79,43%), VORROW (#15, 79,43%), ESTRAVELLE (#16, 79,16%), MARAVEL (#17, 78,88%), KALDRIS (#18, 78,04%), KALDOREN (#19, 77,25%), ORLUNE: The Ringed Tide (#20, 76,96% — cincin batu raksasa di teluk turquoise, judul serif putih besar di atas, tanpa border, tanpa subtitle).

## 7 pola pemenang (dengan bukti)

### 1. Painterly / tekstur litograf vintage mengalahkan flat vector — 8–9 dari top 10
Top 10 didominasi gaya lukis: sapuan painterly, grain kertas, tekstur litograf (#1, #2, #3, #4, #6, #8, #9, #10). Yang flat hanya #5 BALENNE dan #7 HALCYRA — dan keduanya **menebusnya dengan detail sangat padat + komposisi ketat + border**. VELMARIS kita flat DAN sepi: siluet hitam besar nyaris tanpa detail, langit gradien polos. Ini gap terbesar kita.

### 2. Judul serif display BESAR + subtitle/tagline — 9 dari top 10
Hampir semua top 10: nama tempat dalam serif tebal raksasa (biasanya di atas, kadang melintang di landmark) + subtitle letterspaced yang **menjual janji tinggalnya**: "Baths of the Fire Shore", "The Village Inside the Crescent", "Isle of the Sleeping Whale", "Valley of the Second Moon", "The Baths Under the Sea Aqueduct". Subtitle = kriteria juri #2 (janji seperti apa rasanya tinggal di sana). VELMARIS: nama saja, tanpa subtitle, huruf tipis di bawah.

### 3. Border krem / bingkai poster — 6 dari top 10 (+ #1 tepi krem)
#2, #4, #5, #7, #9, #10 punya border krem/ganda yang jelas; #1 tepi krem tipis. Border langsung memberi sinyal "poster travel vintage" dan merapikan komposisi. VELMARIS: tanpa border sama sekali.

### 4. Satu landmark sureal yang jelas + kehidupan manusia
Motif yang berulang: **kota di atas paus** (#3, #5), **cincin/busur batu raksasa** (#7, #10, #20), **mercusuar** (#7, #8), **kota terapung/aneh** (#6 ubur-ubur). Dan hampir semua top 10 ada manusia/aktivitas: berendam, kafe, perahu, lampion, jendela menyala — ini yang membuat juri "pengen pergi" (kriteria #2). VELMARIS punya konsep bagus (pulau melayang + air terjun) tapi **tanpa satu pun manusia/aktivitas**: tidak ada perahu, pemandian, jendela menyala, atau orang.

### 5. Kontras hangat–dingin, cahaya emas
Dominan: matahari terbenam emas/oranye + laut teal/turquoise (#2, #4, #5, #10, #20), atau malam teal gelap + cahaya lampu emas (#3, #6, #8, #9). Cahaya selalu punya sumber dan arah (sun-path di air, jendela menyala, lampion). VELMARIS punya gradien sunset tapi mataharinya cakram datar tanpa sun-path di laut, dan siluet gelap menelan ~40% frame.

### 6. Kota pesisir Mediterania mendominasi — tapi konsepnya harus khas
7+ dari top 10 adalah kota pesisir/tebing ala Mediterania (bangunan putih, atap terracotta, bougainvillea). Yang membedakan bukan settingnya, melainkan **satu twist sureal yang spesifik** (paus, ubur-ubur, cincin, bulan kedua). VELMARIS sudah punya twist (pulau melayang + air terjun ke laut) — konsepnya tidak perlu diganti, eksekusinya yang harus naik kelas.

### 7. Detail padat tapi bermakna, foreground memberi kedalaman
Top 10 penuh detail kecil yang menjual "tempat tinggal": jendela menyala, lampion, bunga, perahu, refleksi, tangga, handuk di batu (#4). Foreground dipakai untuk framing: bougainvillea (#1, #5), balustrade (#5), kolam (#10). VELMARIS: foreground nyaris kosong (laut datar + tebing hitam kanan bawah), tanpa framing.

## Pembeda rank 1–5 vs rank 50+

- **Rank 50 — VESSARO (73,14%)**: flat seperti kita, komposisi sebenarnya kuat (lengkung raksasa membingkai lonceng menyala, orang kecil, perahu). Tapi: detail lebih sedikit, judul melengkung mengikuti arch (tipografi lebih lemah), **tanpa subtitle**, tanpa tekstur. Flat bisa sampai rank 50 — tapi tidak ke top 10 tanpa detail/border/subtitle.
- **Rank 80 — ORUVANE (71,36%)**: painterly, satu menara kaca + satu sosok penyendiri, moody. Judul sans tebal polos di bawah, **tanpa subtitle**, palet muram, tanpa aktivitas/kehidupan. Masih lolos potong 80 karena painterly + komposisi bersih — tapi suasana "sepi" membatasi.
- **Rank 151 — ALVERRA (66,80%)**: painterly, kota tebing + air terjun raksasa — konsep kuat. Tapi judul serif tipis kecil di atas, **tanpa border, tanpa subtitle**, komposisi vertikal membuang ruang square. Tipografi lemah = kalah di kriteria #4.
- **Pola**: makin ke bawah, yang hilang berurutan adalah: (a) subtitle/janji tinggal, (b) border, (c) detail/kehidupan, (d) bobot tipografi. Top 5 punya keempatnya sekaligus.

## Gap entry kita — VELMARIS (dilihat langsung)

**Kekuatan yang sudah ada:**
- Konsep khas & mudah dibaca: pulau melayang + air terjun + mercusuar + matahari besar — sejalan dengan motif pemenang (pulau/paus melayang, cincin).
- Nama terbaca, ejaan jelas, penempatan bawah tidak bentrok dengan landmark utama.
- Palet sunset ungu–oranye–teal senada dengan pemenang; komposisi simetris-ish (2 pulau mengapit matahari).
- Ukuran file kecil (51.874 B) — tie-break ukuran menguntungkan kalau seri rate.

**Gap (urut dampak):**
1. **Terlalu sepi / datar** — siluet hitam besar tanpa detail: tidak ada jendela menyala, orang, perahu, atau aktivitas. Kriteria juri #2 (janji tinggal) nyaris nol. Bandingkan #7 HALCYRA: flat juga, tapi ada desa + perahu + refleksi + sunburst.
2. **Tanpa subtitle/tagline** — 9/10 top 10 punya. Tanpa janji tekstual, poster hanya "pemandangan indah", bukan "tempat yang pengen dikunjungi".
3. **Tanpa border** — 6/10 top 10 punya; border adalah sinyal "poster" termurah.
4. **Tipografi tipis** — huruf VELMARIS tipis, letterspaced, di bawah, duduk di atas garis laut/tebing yang ramai. Top 10 pakai serif tebal, biasanya di atas atau terintegrasi ke landmark (#1 bayangan di lantai, #3 di badan paus).
5. **Matahari cakram datar, tanpa sun-path** — laut di bawah matahari polos; top 10 selalu punya pantulan cahaya di air.
6. **Tidak ada foreground framing** — sudut bawah kosong; top 10 memakai bunga/balustrade/batu/kolam.
7. **Langit gradien polos** — bintang kecil tersebar acak; bandingkan tekstur awan/grain top 10.

## Rekomendasi konkret untuk revisi (prioritas)

1. **Tambah kehidupan + detail pada siluet** (dampak terbesar): jendela/lampu menyala di pulau melayang, 1–2 perahu kecil di laut, sosok kecil di dermaga/tebing, burung sudah ada — pertahankan. Ini yang mengangkat kriteria #2.
2. **Tambah subtitle di bawah VELMARIS**, mis. "THE ISLES ABOVE THE FALLS" / "WHERE THE ISLANDS DRIFT" — huruf kecil letterspaced, krem. Menjual janji tinggal + meniru pola 9/10 top 10.
3. **Tambah border krem ganda** (tipis, ~8–12 px + garis dalam) — sinyal poster instan, murah dikerjakan.
4. **Tebalkan judul**: serif lebih berat (atau pertahankan art-deco tapi naikkan weight + sedikit ukuran), dan/atau pindah ke atas. Minimal: beri outline/shadow halus supaya tidak tenggelam di garis laut.
5. **Sun-path di laut**: pantulan cahaya emas vertikal di bawah matahari + sedikit riak; tambah tekstur grain halus di langit dan laut.
6. **Foreground**: batu/bunga di sudut bawah, atau dermaga kecil dengan lampion di kanan bawah — memberi kedalaman dan framing.
7. **JANGAN ganti konsep** (pulau melayang + air terjun + mercusuar sudah khas dan sejalan dengan motif pemenang). Yang diperbaiki hanya eksekusi: detail, tipografi, border, cahaya.
8. **Jaga ukuran ≤1 MiB dan 1024×1024** (saat ini 51.874 B — masih sangat longgar; detail painterly masih muat).

## Untuk Goldfish review

- Analisis ini + entry VELMARIS saat ini = bahan review. Verdict yang dicari: LAYAK LANJUT / perbaikan di atas dulu, lalu resubmit.
- Ekspektasi jujur: VELMARIS versi saat ini (flat, sepi, tanpa subtitle/border) secara pola lebih dekat ke rank 50–150 (rate ~67–73%) daripada top 20. Dengan revisi 1–6 di atas, target masuk 80 besar (≥71,4%) realistis; zona hadiah (≥77%) butuh eksekusi painterly yang kuat — berat dicapai dari base flat dalam 1 sesi revisi, tapi patut dicoba karena kuota masih ada.
- Kuota (pre-open): entries_made 0, day 3 left, hard 20 left (catatan state file 10:12 WIB — verifikasi ulang saat submit).
- Deadline 15:39 WIB; snapshot ini 14:12 WIB — sisa ~1 jam 27 mnt saat analisis ditulis.

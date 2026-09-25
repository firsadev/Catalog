import os

html_content = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Katalog PDF - DHJIE Sound System Production</title>
    <meta name="description" content="Katalog Resmi Sewa Sound System, Panggung Rigging, Lighting Stage, Videotron LED P3.1, Tenda Sarnafil & Alat Musik - DHJIE Sound System Production Bogor">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --bg-dark: #06080d;
            --bg-card: rgba(18, 22, 32, 0.88);
            --accent-gold: #f1c40f;
            --accent-gold-dark: #d4ac0d;
            --accent-gold-glow: rgba(241, 196, 15, 0.35);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-gold: rgba(241, 196, 15, 0.35);
            --border-glass: rgba(255, 255, 255, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #0b0d14;
            color: var(--text-main);
            line-height: 1.5;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }

        /* Top Bar Navigation for Screen Viewing */
        .top-toolbar {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(7, 9, 14, 0.92);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-gold);
            padding: 12px 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }

        .toolbar-brand {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: #fff;
        }

        .brand-icon {
            width: 42px;
            height: 42px;
            background: linear-gradient(135deg, var(--accent-gold), #d35400);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #000;
            font-size: 20px;
            box-shadow: 0 0 15px var(--accent-gold-glow);
        }

        .brand-title {
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: 16px;
            letter-spacing: 1px;
            color: #fff;
        }

        .brand-subtitle {
            font-size: 11px;
            color: var(--accent-gold);
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 700;
        }

        .toolbar-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 18px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.25s ease;
            text-decoration: none;
            border: none;
        }

        .btn-gold {
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
            color: #000;
            box-shadow: 0 4px 15px var(--accent-gold-glow);
        }

        .btn-gold:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(241, 196, 15, 0.5);
        }

        .btn-wa {
            background: #25D366;
            color: #fff;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        }

        .btn-wa:hover {
            background: #20ba5a;
            transform: translateY(-2px);
        }

        .badge-pages {
            background: rgba(241, 196, 15, 0.15);
            border: 1px solid var(--border-gold);
            color: var(--accent-gold);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Catalog Screen Preview Container */
        .pdf-catalog-wrapper {
            padding: 30px 15px 60px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 30px;
        }

        /* Printable A4 Page Container */
        .printable-page {
            width: 210mm;
            height: 297mm;
            background: #06080d;
            color: #fff;
            position: relative;
            overflow: hidden;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.8), 0 0 1px rgba(241, 196, 15, 0.4);
            border: 1px solid rgba(241, 196, 15, 0.3);
            border-radius: 4px;
            page-break-after: always;
            break-after: page;
        }

        .page-stage-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
            opacity: 0.18;
            z-index: 1;
            filter: blur(2px);
        }

        .page-inner-container {
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            padding: 20mm 18mm;
        }

        /* Page Headers & Footers */
        .pdf-brand-hdr {
            border-bottom: 2px solid var(--border-gold);
            padding-bottom: 10px;
            margin-bottom: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .pdf-brand-hdr h2 {
            font-family: 'Montserrat', sans-serif;
            font-size: 15px;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 800;
        }

        .pdf-brand-hdr .page-num {
            font-family: 'Montserrat', sans-serif;
            font-size: 12px;
            font-weight: 800;
            color: var(--accent-gold);
            background: rgba(241, 196, 15, 0.12);
            padding: 4px 12px;
            border-radius: 12px;
            border: 1px solid var(--border-gold);
        }

        .pdf-section-title {
            font-family: 'Montserrat', sans-serif;
            font-size: 20px;
            font-weight: 900;
            color: var(--accent-gold);
            margin-bottom: 16px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-left: 5px solid var(--accent-gold);
            padding-left: 12px;
        }

        /* Card Content Design */
        .pdf-card {
            background: var(--bg-card);
            border: 1px solid var(--border-gold);
            border-radius: 12px;
            padding: 16px;
            backdrop-filter: blur(10px);
            margin-bottom: 16px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        }

        .pdf-card-title {
            font-family: 'Montserrat', sans-serif;
            font-size: 16px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 6px;
        }

        .pdf-price-tag {
            font-family: 'Montserrat', sans-serif;
            font-size: 15px;
            font-weight: 800;
            color: var(--accent-gold);
            margin-bottom: 12px;
            display: inline-block;
            background: rgba(241, 196, 15, 0.12);
            padding: 4px 12px;
            border-radius: 6px;
            border: 1px solid var(--border-gold);
        }

        .pdf-specs-list {
            list-style: none;
            padding-left: 0;
        }

        .pdf-specs-list li {
            font-size: 12px;
            color: #e2e8f0;
            margin-bottom: 6px;
            display: flex;
            align-items: flex-start;
            gap: 8px;
            line-height: 1.4;
        }

        .pdf-specs-list li i {
            color: var(--accent-gold);
            font-size: 11px;
            margin-top: 3px;
            flex-shrink: 0;
        }

        .pdf-img-box {
            width: 100%;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.15);
            margin-bottom: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }

        .pdf-img-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .pdf-footer-content {
            border-top: 1px solid var(--border-gold);
            padding-top: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 10.5px;
            color: var(--text-muted);
        }

        .pdf-footer-content strong {
            color: var(--accent-gold);
        }

        /* PRINT STYLES - Exact A4 output */
        @media print {
            @page {
                size: A4 portrait;
                margin: 0;
            }
            body {
                background: none !important;
                color: #000 !important;
            }
            .top-toolbar {
                display: none !important;
            }
            .pdf-catalog-wrapper {
                padding: 0 !important;
                gap: 0 !important;
            }
            .printable-page {
                margin: 0 !important;
                box-shadow: none !important;
                border: none !important;
                border-radius: 0 !important;
                page-break-after: always !important;
                break-after: page !important;
                width: 210mm !important;
                height: 297mm !important;
                max-height: 297mm !important;
                overflow: hidden !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
        }
    </style>
</head>
<body>

    <!-- TOP TOOLBAR -->
    <header class="top-toolbar">
        <div class="toolbar-brand">
            <div class="brand-icon">
                <i class="fa-solid fa-compact-disc"></i>
            </div>
            <div>
                <div class="brand-title">DHJIE SOUNDSYSTEM PRODUCTION</div>
                <div class="brand-subtitle">Official PDF Event Catalog</div>
            </div>
        </div>

        <div class="toolbar-actions">
            <div class="badge-pages">
                <i class="fa-solid fa-file-pdf"></i> 14 Halaman A4
            </div>
            <button class="btn btn-gold" onclick="window.print()">
                <i class="fa-solid fa-print"></i> Cetak / Simpan PDF (Ctrl+P)
            </button>
            <a href="https://wa.me/6289638626771?text=Halo%20Dhjie%20Soundsystem%20Production,%20saya%20ingin%20konsultasi%20sewa%20peralatan" target="_blank" class="btn btn-wa">
                <i class="fa-brands fa-whatsapp"></i> WA: 0896-3862-6771
            </a>
        </div>
    </header>

    <!-- FULL 14-PAGE PDF CATALOG CONTAINER -->
    <div class="pdf-catalog-wrapper">

        <!-- HALAMAN 1: COVER -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1200&q=80'); opacity: 0.35; filter: none;"></div>
            <div class="page-inner-container" style="text-align: center;">
                <div style="margin-top: 15px;">
                    <div style="font-family: 'Montserrat', sans-serif; font-size: 34px; font-weight: 900; letter-spacing: 2px; color: #fff;">DHJIE SOUNDSYSTEM</div>
                    <div style="font-size: 18px; font-weight: 800; letter-spacing: 5px; color: var(--accent-gold); text-transform: uppercase;">PRODUCTION & EVENT SUPPLIER</div>
                </div>

                <div style="margin: auto 0; background: rgba(11, 14, 22, 0.85); border: 1px solid var(--border-gold); padding: 35px 20px; border-radius: 16px; backdrop-filter: blur(12px);">
                    <div style="font-family: 'Montserrat', sans-serif; font-size: 64px; font-weight: 900; color: var(--accent-gold); letter-spacing: 6px; text-shadow: 0 4px 30px rgba(241,196,15,0.4); margin-bottom: 10px;">
                        CATALOG
                    </div>
                    <div style="font-size: 13px; color: #e2e8f0; letter-spacing: 1.5px; line-height: 2; max-width: 620px; margin: 0 auto; text-transform: uppercase; font-weight: 700;">
                        Soundsystem • Panggung Rigging • Stage Lighting • Videotron LED P3.1 • Tenda Sarnafil • Alat Musik • Genset • Barikade • Backdrop Custom
                    </div>
                </div>

                <div style="border-top: 2px solid var(--border-gold); padding-top: 18px; display: flex; justify-content: space-between; align-items: flex-end; text-align: left;">
                    <div style="font-size: 12px; line-height: 1.6; color: #cbd5e1; max-width: 420px;">
                        <strong style="color: var(--accent-gold); font-size: 13px;">Alamat Workshop & Kantor:</strong><br>
                        Perumahan Billabong Permai D3D, Jl. Pangrango VII No. 8, Bojonggede, Bogor, Jawa Barat
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">Reservasi WhatsApp</div>
                        <div style="font-family: 'Montserrat', sans-serif; font-size: 22px; font-weight: 900; color: var(--accent-gold);">0896-3862-6771</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 2: ANEKA PANGGUNG -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 02</span>
                    </div>
                    <div class="pdf-section-title">Aneka Panggung</div>

                    <div class="pdf-card">
                        <div class="pdf-img-box" style="height: 230px;">
                            <img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=1000&q=80" alt="Panggung Rigging">
                        </div>
                        <div class="pdf-card-title">Panggung Rigging Aluminium</div>
                        <div class="pdf-price-tag">Harga: Rp 200.000 / meter</div>
                        <ul class="pdf-specs-list">
                            <li><i class="fa-solid fa-circle-check"></i> <span>Konstruksi Truss Aluminium Rigging Heavy Duty & Kokoh</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Dilengkapi Atap Canvas Terpal Anti-Air & Karpet Stage Clean</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Ketinggian Level Panggung (50 cm – 1.5 meter) Sesuai Request Event</span></li>
                        </ul>
                    </div>

                    <div class="pdf-card">
                        <div class="pdf-img-box" style="height: 230px;">
                            <img src="https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?auto=format&fit=crop&w=1000&q=80" alt="Panggung Custom">
                        </div>
                        <div class="pdf-card-title">Panggung Custom / Level Event</div>
                        <div class="pdf-price-tag">Harga: Rp 200.000 – Rp 500.000 / meter</div>
                        <ul class="pdf-specs-list">
                            <li><i class="fa-solid fa-circle-check"></i> <span>Desain Formasi Custom (T-Shape, Catwalk, Circular, Multiple Level)</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Finishing Karpet Hitam/Merah Premium atau Melamin Glossy</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Sangat Ideal untuk Fashion Show, Exhibition, Awarding & Corporate Event</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 3: ANEKA BACKDROP -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 03</span>
                    </div>
                    <div class="pdf-section-title">Aneka Backdrop Event</div>

                    <div class="pdf-card" style="padding: 24px;">
                        <div class="pdf-img-box" style="height: 400px;">
                            <img src="https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1000&q=80" alt="Backdrop Custom">
                        </div>
                        <div class="pdf-card-title" style="font-size: 20px;">Backdrop Standar & Custom Pop-Up 3D</div>
                        <div class="pdf-price-tag" style="font-size: 16px;">Harga: Rp 250.000 / meter</div>
                        <ul class="pdf-specs-list" style="margin-top: 10px;">
                            <li><i class="fa-solid fa-circle-check"></i> <span>Rangka Kayu Solid & Printing Flexi Korea High Resolution</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Opsi Model Pop-Up 3D Custom dengan Aksen LED Strip Lighting</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Sudah Termasuk Jasa Pemasangan & Bongkaran Area Bogor & Jabodetabek</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Rapi, Presisi, dan Siap Pakai untuk Seminar, Concert & Gathering</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 4: ANEKA TENDA & KURSI -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 04</span>
                    </div>
                    <div class="pdf-section-title">Aneka Tenda & Kursi Event</div>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div class="pdf-card">
                            <div class="pdf-img-box" style="height: 250px;">
                                <img src="https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=800&q=80" alt="Tenda Sarnafil">
                            </div>
                            <div class="pdf-card-title">Tenda Sarnafil Kerucut</div>
                            <div class="pdf-price-tag">Sarnafil 3x3m : Rp 350.000 / unit</div>
                            <div class="pdf-price-tag" style="margin-top:-4px;">Sarnafil 5x5m : Rp 650.000 / unit</div>
                            <ul class="pdf-specs-list">
                                <li><i class="fa-solid fa-circle-check"></i> <span>Terpal Kerucut Sarnafil Putih Clean</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Rangka Aluminium Rapi & Kokoh</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Lengkap Dinding Penutup Samping</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Cocok untuk Booth Bazar & VIP</span></li>
                            </ul>
                        </div>

                        <div class="pdf-card">
                            <div class="pdf-img-box" style="height: 250px;">
                                <img src="https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=800&q=80" alt="Tenda VIP & Kursi">
                            </div>
                            <div class="pdf-card-title">Tenda VIP & Kursi Futura</div>
                            <div class="pdf-price-tag">Tenda VIP : Rp 50.000 – Rp 85.000 / m²</div>
                            <div class="pdf-price-tag" style="margin-top:-4px;">Kursi Futura : Rp 10.000 – Rp 15.000 / unit</div>
                            <ul class="pdf-specs-list">
                                <li><i class="fa-solid fa-circle-check"></i> <span>Kursi Futura Polos : Rp 10.000 / unit</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Futura + Cover Press Fit & Pita : Rp 15.000</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Tenda Dekorasi VIP Serut Elegant</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Kondisi Busa Empuk & Clean</span></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 5: ALAT MUSIK -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 05</span>
                    </div>
                    <div class="pdf-section-title">Alat Musik & Backline Stage</div>

                    <div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 16px; background: var(--bg-card); border: 1px solid var(--border-gold); border-radius: 12px; padding: 20px;">
                        <div>
                            <div style="font-size: 13px; line-height: 1.8; color: #fff;">
                                <div style="margin-bottom: 8px;">
                                    <strong style="color: var(--accent-gold);">GUITAR ELEKTRIK YAMAHA PACIFICA:</strong><br>
                                    <span style="font-size: 14px; font-weight: 800;">Rp 300.000 / unit</span> (Include Softcase & Cable)
                                </div>
                                <div style="margin-bottom: 8px;">
                                    <strong style="color: var(--accent-gold);">BASS ELEKTRIK YAMAHA BB234:</strong><br>
                                    <span style="font-size: 14px; font-weight: 800;">Rp 300.000 / unit</span> (Include Strap & Cable)
                                </div>
                                <div style="margin-bottom: 8px;">
                                    <strong style="color: var(--accent-gold);">KEYBOARD & STAGE PIANO:</strong>
                                    <ul style="padding-left: 18px; font-size: 12px; color: #cbd5e1; margin-top: 4px;">
                                        <li>Rolland BK3 / Juno : Rp 400.000</li>
                                        <li>Yamaha PSR290 / Korg PA1000 : Rp 400.000</li>
                                        <li>Stage Piano Roland RD 700 : Rp 700.000</li>
                                    </ul>
                                </div>
                                <div style="margin-bottom: 8px;">
                                    <strong style="color: var(--accent-gold);">DRUM SET ACOUSTIC & DIGITAL:</strong>
                                    <ul style="padding-left: 18px; font-size: 12px; color: #cbd5e1; margin-top: 4px;">
                                        <li>Yamaha DTX6K3X Digital Drum : Rp 600.000</li>
                                        <li>Tama Superstar Classic Acoustic : Rp 700.000</li>
                                        <li>Mic Drum Set AKG Professional : Rp 300.000</li>
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div style="display: flex; flex-direction: column; gap: 10px;">
                            <div class="pdf-img-box" style="height: 140px; margin-bottom: 0;">
                                <img src="https://images.unsplash.com/photo-1564186763535-ebb21ef5277f?auto=format&fit=crop&w=600&q=80" alt="Guitar Yamaha">
                            </div>
                            <div class="pdf-img-box" style="height: 140px; margin-bottom: 0;">
                                <img src="https://images.unsplash.com/photo-1525994886773-0805aa7cc1a2?auto=format&fit=crop&w=600&q=80" alt="Keyboard Synthesizer">
                            </div>
                            <div class="pdf-img-box" style="height: 150px; margin-bottom: 0;">
                                <img src="https://images.unsplash.com/photo-1519892300165-cb5542fb47c7?auto=format&fit=crop&w=600&q=80" alt="Drum Set Tama">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 6: VIDEOTRON -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 06</span>
                    </div>
                    <div class="pdf-section-title">Videotron Stage High Resolution</div>

                    <div class="pdf-card" style="padding: 24px;">
                        <div class="pdf-img-box" style="height: 380px;">
                            <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=1000&q=80" alt="Videotron P3.1">
                        </div>
                        <div class="pdf-card-title" style="font-size: 20px;">Videotron LED Display P3.1 Indoor / Outdoor</div>
                        <div class="pdf-price-tag" style="font-size: 16px;">Harga: Rp 600.000 / m²</div>
                        <ul class="pdf-specs-list" style="margin-top: 10px;">
                            <li><i class="fa-solid fa-circle-check"></i> <span>Spesifikasi Modul LED Pixel Pitch P3.1 Ultra Sharp Resolution</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Ketinggian Level Sub-structure Panggung 50 cm – 100 cm</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Include 1 Unit Control Laptop Master & Operator Video Standby Full Event</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Sangat Cocok untuk Concert Background, Presentation & Live Visual</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 7: PAKET LIGHTING -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 07</span>
                    </div>
                    <div class="pdf-section-title">Paket Lighting Panggung</div>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div class="pdf-card">
                            <div class="pdf-img-box" style="height: 250px;">
                                <img src="https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?auto=format&fit=crop&w=800&q=80" alt="Paket Lighting A">
                            </div>
                            <div class="pdf-card-title">Paket Stage Lighting A</div>
                            <div class="pdf-price-tag">Harga: Rp 3.500.000</div>
                            <ul class="pdf-specs-list">
                                <li><i class="fa-solid fa-circle-check"></i> <span>8 Unit Parled TRF Spotlight</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>4 Unit Moving Beam Clara S</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>5 Unit Strobo Flash Light</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>2 Unit Fresnel Warm Light + Stand</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Mixer Lighting Kingkong Console</span></li>
                            </ul>
                        </div>

                        <div class="pdf-card">
                            <div class="pdf-img-box" style="height: 250px;">
                                <img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=800&q=80" alt="Paket Lighting B">
                            </div>
                            <div class="pdf-card-title">Paket Stage Lighting B</div>
                            <div class="pdf-price-tag">Harga: Rp 2.500.000</div>
                            <ul class="pdf-specs-list">
                                <li><i class="fa-solid fa-circle-check"></i> <span>8 Unit Parled TRF Spotlight</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>2 Unit Moving Beam Clara S</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>4 Unit Strobo Flash Light</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>2 Unit Fresnel Warm Light + Stand</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Mixer Lighting Kingkong E Console</span></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 8: SOUND 2.000W & 3.000W -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1545128485-c400e7702796?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 08</span>
                    </div>
                    <div class="pdf-section-title">Sound System Standard Capacity</div>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                        <div class="pdf-card">
                            <div class="pdf-img-box" style="height: 250px;">
                                <img src="https://images.unsplash.com/photo-1545128485-c400e7702796?auto=format&fit=crop&w=800&q=80" alt="Paket 2000W">
                            </div>
                            <div class="pdf-card-title">Paket Sound 2.000 Watt</div>
                            <div class="pdf-price-tag">Harga: Rp 2.000.000</div>
                            <ul class="pdf-specs-list">
                                <li><i class="fa-solid fa-circle-check"></i> <span>2 Unit Sub + Triway Turbosound IP2000</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>2 Unit Monitor Turbosound Milan M15</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Mixer AD Live Pro Console</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Mic Wireless Hardwell & Shure SM58</span></li>
                            </ul>
                        </div>

                        <div class="pdf-card">
                            <div class="pdf-img-box" style="height: 250px;">
                                <img src="https://images.unsplash.com/photo-1520523839896-5aa428633bc8?auto=format&fit=crop&w=800&q=80" alt="Paket 3000W">
                            </div>
                            <div class="pdf-card-title">Paket Sound 3.000 Watt</div>
                            <div class="pdf-price-tag">Harga: Rp 3.000.000</div>
                            <ul class="pdf-specs-list">
                                <li><i class="fa-solid fa-circle-check"></i> <span>2 Unit Sub Turbosound IP2000</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>3 Unit Monitor Turbosound Milan M15</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Mixer Midas M32R + DL 32 Midas</span></li>
                                <li><i class="fa-solid fa-circle-check"></i> <span>Mic Wireless Hardwell & Shure SM58</span></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 9: SOUND 5.000 WATT -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 09</span>
                    </div>
                    <div class="pdf-section-title">Sound System 5.000 Watt</div>

                    <div class="pdf-card" style="padding: 24px;">
                        <div class="pdf-img-box" style="height: 380px;">
                            <img src="https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=1000&q=80" alt="Sound 5000W">
                        </div>
                        <div class="pdf-card-title" style="font-size: 20px;">Kapasitas 5.000 Watt Professional</div>
                        <div class="pdf-price-tag" style="font-size: 16px;">Harga: Rp 5.000.000</div>
                        <ul class="pdf-specs-list" style="margin-top: 10px;">
                            <li><i class="fa-solid fa-circle-check"></i> <span>PA Speaker: 2 Unit Sub Evo / IP2000 & 2 Unit Yamaha DSR Active</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Stage Monitor: 4 Unit Turbosound Milan M15 High Clarity</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Mixer System: Midas M32R + DL 32 Midas Digital Snake System</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Aksesoris: Mic Wireless Hardwell, Shure SM58, Mic Drum Kit AKG & DI Box</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 10: SOUND 10.000 WATT -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 10</span>
                    </div>
                    <div class="pdf-section-title">Sound System 10.000 Watt</div>

                    <div class="pdf-card" style="padding: 24px;">
                        <div class="pdf-img-box" style="height: 380px;">
                            <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1000&q=80" alt="Sound 10000W">
                        </div>
                        <div class="pdf-card-title" style="font-size: 20px;">Kapasitas 10.000 Watt Concert Grade</div>
                        <div class="pdf-price-tag" style="font-size: 16px;">Harga: Rp 10.000.000</div>
                        <ul class="pdf-specs-list" style="margin-top: 10px;">
                            <li><i class="fa-solid fa-circle-check"></i> <span>PA Speaker: 4 Unit Subwoofer TTS36218, 4 Unit Line Array Vera 110, Low Pack 115</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Stage Monitor: 6 Unit Milan M15 & Ear Monitor Behringer P1</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Mixer System: Midas M32R & M32 Live + DL 32 Midas Stagebox</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Komunikasi Intercom: Clearcom Hollyland Wireless Intercom System</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 11: SOUND 15.000 WATT -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 11</span>
                    </div>
                    <div class="pdf-section-title">Sound System 15.000 Watt</div>

                    <div class="pdf-card" style="padding: 24px;">
                        <div class="pdf-img-box" style="height: 380px;">
                            <img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=1000&q=80" alt="Sound 15000W">
                        </div>
                        <div class="pdf-card-title" style="font-size: 20px;">Kapasitas 15.000 Watt High Output</div>
                        <div class="pdf-price-tag" style="font-size: 16px;">Harga: Rp 15.000.000</div>
                        <ul class="pdf-specs-list" style="margin-top: 10px;">
                            <li><i class="fa-solid fa-circle-check"></i> <span>PA Speaker: 6 Unit Subwoofer TTS36218, 4 Unit Vera 110, Low Pack 115</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Monitor System: 6 Unit Turbosound Milan M15, 4 Unit In-Ear Monitor P1</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Mixer & Control: Midas M32R, M32 Live, DL 32 Stagebox</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Intercom System: Clearcom Hollyland Wireless Intercom Setup</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 12: SOUND 20.000 WATT -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 12</span>
                    </div>
                    <div class="pdf-section-title">Sound System 20.000 Watt Concert Level</div>

                    <div class="pdf-card" style="padding: 24px;">
                        <div class="pdf-img-box" style="height: 380px;">
                            <img src="https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?auto=format&fit=crop&w=1000&q=80" alt="Sound 20000W">
                        </div>
                        <div class="pdf-card-title" style="font-size: 20px;">Kapasitas 20.000 Watt Arena Concert</div>
                        <div class="pdf-price-tag" style="font-size: 16px;">Harga: Rp 20.000.000</div>
                        <ul class="pdf-specs-list" style="margin-top: 10px;">
                            <li><i class="fa-solid fa-circle-check"></i> <span>PA Speaker: 8 Unit Subwoofer TTS36218, 8 Unit Line Array RDW Tara123</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Monitor Stage: 8 Unit Milan M15, 2 Unit Side Fill Yamaha DSR 215 High Power</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Control Desk: Midas M32R & M32 Live + DL 32 Midas Stagebox</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Intercom System: Clearcom Hollyland Wireless Intercom Crew System</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 13: SOUND 40.000 WATT -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1000&q=80');"></div>
            <div class="page-inner-container">
                <div>
                    <div class="pdf-brand-hdr">
                        <h2>DHJIE SOUNDSYSTEM PRODUCTION</h2>
                        <span class="page-num">Halaman 13</span>
                    </div>
                    <div class="pdf-section-title">Sound System 40.000 Watt Stadium Level</div>

                    <div class="pdf-card" style="padding: 24px;">
                        <div class="pdf-img-box" style="height: 380px;">
                            <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1000&q=80" alt="Sound 40000W">
                        </div>
                        <div class="pdf-card-title" style="font-size: 20px;">Kapasitas 40.000 Watt Stadium Concert Flagship</div>
                        <div class="pdf-price-tag" style="font-size: 16px;">Harga: Rp 40.000.000</div>
                        <ul class="pdf-specs-list" style="margin-top: 10px;">
                            <li><i class="fa-solid fa-circle-check"></i> <span>PA Speaker: 16 Unit Subwoofer TTS36218, 16 Unit Line Array RDW Tara123</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Monitor Stage: 10 Unit Milan M15, 2 Unit Side Fill Yamaha DSR215 Stadium Output</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Mixing & Control: Dual Midas M32 Consoles, DL 32 Stagebox, Full Mic Rigging</span></li>
                            <li><i class="fa-solid fa-circle-check"></i> <span>Super Stadium Class Clarity, Power & Professional Engineering Team</span></li>
                        </ul>
                    </div>
                </div>

                <div class="pdf-footer-content">
                    <div><strong>WhatsApp:</strong> 0896-3862-6771</div>
                    <div><strong>Workshop:</strong> Perumahan Billabong Permai D3D, Bojonggede, Bogor</div>
                </div>
            </div>
        </div>

        <!-- HALAMAN 14: COVER PENUTUP & KONTAK -->
        <div class="printable-page">
            <div class="page-stage-bg" style="background-image: url('https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=1200&q=80'); opacity: 0.35; filter: none;"></div>
            <div class="page-inner-container" style="text-align: center; justify-content: center;">
                <div style="margin-bottom: 30px;">
                    <div style="font-family: 'Montserrat', sans-serif; font-size: 38px; font-weight: 900; letter-spacing: 2px;">DHJIE SOUNDSYSTEM</div>
                    <div style="font-size: 20px; font-weight: 800; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 4px;">PRODUCTION & EVENT SUPPLIER</div>
                </div>

                <div style="font-family: 'Montserrat', sans-serif; font-size: 22px; color: var(--accent-gold); margin-bottom: 30px; font-weight: 800; text-transform: uppercase;">
                    Terima Kasih Atas Kepercayaan Anda
                </div>

                <div style="margin: 0 auto 35px; max-width: 550px; font-size: 14px; color: #e2e8f0; line-height: 1.8; background: rgba(11, 14, 22, 0.85); border: 1px solid var(--border-gold); border-radius: 16px; padding: 25px; backdrop-filter: blur(12px);">
                    <strong style="color: var(--accent-gold); font-size: 16px;">Workshop & Office:</strong><br>
                    Perumahan Billabong Permai D3D, Jl. Pangrango VII No. 8, Bojonggede, Bogor, Jawa Barat
                </div>

                <div style="text-align: center;">
                    <div style="font-size: 13px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 700;">Hubungi Kami / Reservasi WhatsApp</div>
                    <div style="font-family: 'Montserrat', sans-serif; font-size: 36px; font-weight: 900; color: var(--accent-gold); margin-top: 6px;">0896-3862-6771</div>
                    <a href="https://wa.me/6289638626771?text=Halo%20Dhjie%20Soundsystem%20Production,%20saya%20ingin%20konsultasi%20sewa%20peralatan" target="_blank" class="btn btn-wa" style="margin-top: 20px; font-size: 15px; padding: 12px 28px;">
                        <i class="fa-brands fa-whatsapp"></i> Chat Direct WhatsApp
                    </a>
                </div>
            </div>
        </div>

    </div>

</body>
</html>

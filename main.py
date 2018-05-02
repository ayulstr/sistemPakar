bab2 = "bab2"
encer = "encer"
darah = "darah"
lesu = "lesu"
t_selera = "t_selera"
mual = "mual"
perut = "perut"
t_darah = "t_darah"
pusing = "pusig"
pingsan = "pingsan"
suhu_tinggi = "suhu_tinggi"
luka = "luka"
t_bergerak = "t_bergerak"
makan = "makan"
daging = "daging"
jamur = "jamur"
kaleng = "kaleng"
b_susu = "b_susu"
m_susu = "m_susu"

sub_gejala = [ bab2, encer, darah, lesu, t_selera, mual, perut, t_darah, pusing, pingsan, suhu_tinggi, luka, t_bergerak, makan, daging, jamur, kaleng, b_susu, m_susu ]

mencret = [
    0,
    [
        lesu,
        t_selera,
        mual
    ]
]
muntah = [
    0,
    [
        lesu,
        t_selera,
        mual
    ]
]
s_perut = [
    0,
    [
        lesu,
        perut
    ]
]
darah_rendah = [
    0,
    [
        lesu,
        t_darah,
        pusing
    ]
]
koma = [
    0,
    [
        t_darah,
        pusing
    ]
]
demam = [
    0,
    [
        lesu,
        t_selera,
        pusing,
        suhu_tinggi
    ]
]
septicaemia = [
    0,
    [
        lesu,
        t_darah,
        suhu_tinggi,
        luka
    ]
]
lumpuh = [
    0,
    [
        lesu,
        t_bergerak
    ]
]
mencret_berdarah = [
    0,
    [
        bab2,
        encer,
        darah,
        lesu,
        t_selera
    ]
]
makan_daging = [
    0,
    [
        makan,
        daging
    ]
]
makan_jamur = [
    0,
    [
        makan,
        jamur
    ]
]
makan_kaleng = [
    0,
    [
        makan,
        kaleng
    ]
]
minum_susu = [
    b_susu,
    m_susu
]

gejala = [mencret, muntah, s_perut, darah_rendah, koma, demam, septicaemia, lumpuh, mencret_berdarah, makan_daging, makan_jamur, makan_kaleng, minum_susu]

staphylococcus = [
    0,
    [
        mencret,
        muntah,
        s_perut,
        darah_rendah,
        makan_daging
    ]
]
jamur_beracun = [
    0,
    [
        mencret,
        muntah,
        s_perut,
        koma,
        makan_jamur
    ]
]
salmonallae = [
    0,
    [
        mencret,
        muntah,
        s_perut,
        demam,
        septicaemia,
        makan_daging
    ]
]
clostridium = [
    0,
    [
        muntah,
        lumpuh,
        makan_kaleng
    ]
]
campylobacter = [
    0,
    [
        mencret_berdarah,
        mencret,
        s_perut,
        demam,
        minum_susu
    ]
]

penyakit = [staphylococcus, jamur_beracun, salmonallae, clostridium, campylobacter]

if __name__ == '__main__':
    bab2 = input('Apakah anda sering mengalami buang air besar (lebih dari 2 kali)? (y/t)')
    if bab2 == 'y':
        bab2 = 'bab2'

    encer = input('Apakah anda mengalami berak encer? (y/t)')
    if encer == 'y':
        encer = 'bab_encer'

    darah = input("Apakah anda mengalami berak berdarah?")
    if darah == 'y':
        darah = 'darah'

    lesu = input("Apakah anda merasa lesu dan tidak bergairah?")
    if lesu == 'y':
        lesu = 'lesu'

    t_selera = input("Apakah anda tidak selera makan?")
    if t_selera == 'y':
        t_selera = 't_selera'

    mual = input("Apakah anda merasa mual dan sering muntah (lebih dari 1 kali) ?")
    if mual == 'y':
        mual = 'mual'

    perut = input("Apakah anda merasa sakit di bagian perut ?")
    if perut == 'y':
        perut = 'perut'

    t_darah = input("Apakah tekanan darah anda rendah ?")
    if t_darah == 'y':
        t_darah = 't_darah'

    pusing = input("Apakah anda merasa pusing ?")
    if pusing == 'y':
        pusing = 'pusing'

    pingsan = input("Apakah anda mengalami pingsan ?")
    if pingsan == 'y':
        pingsan = 'pingsan'

    suhu_tinggi = input("Apakah suhu badan anda tinggi ?")
    if suhu_tinggi == 'y':
        suhu_tinggi = 'suhu_tinggi'

    luka = input("Apakah anda mengalami luka di bagian tertentu ?")
    if luka == 'y':
        luka = 'luka'

    t_bergerak = input("Apakah anda tidak dapat menggerakkan anggota badan tertentu ?")
    if t_bergerak == 'y':
        t_bergerak = 't_bergerak'

    makan = input("Apakah anda pernah memakan sesuatu ?")
    if makan == 'y':
        makan = 'makan'

    daging = input("Apakah anda memakan daging ?")
    if daging == 'y':
        daging = 'daging'

    jamur = input("Apakah anda memakan jamur ?")
    if jamur == 'y':
        jamur = 'jamur'

    kaleng = input("Apakah anda memakan makanan kaleng ?")
    if kaleng == 'y':
        kaleng = 'kaleng'

    b_susu = input("Apakah anda membeli susu ?")
    if b_susu == 'y':
        b_susu = 'm_susu'

    m_susu = input("Apakah anda meminum susu ?")
    if m_susu == 'y':
        m_susu = 's_perut'

    sub_gejala = [bab2, encer, darah, lesu, t_selera, mual, perut, t_darah, pusing, pingsan, suhu_tinggi, luka, t_bergerak, makan, daging, jamur, kaleng, b_susu, m_susu]
    # print(sub_gejala)

    mencret = [
        0.0,
        [
            lesu,
            t_selera,
            mual
        ]
    ]
    muntah = [
        0.0,
        [
            lesu,
            t_selera,
            mual
        ]
    ]
    s_perut = [
        0.0,
        [
            lesu,
            perut
        ]
    ]
    darah_rendah = [
        0.0,
        [
            lesu,
            t_darah,
            pusing
        ]
    ]
    koma = [
        0.0,
        [
            t_darah,
            pusing
        ]
    ]
    demam = [
        0.0,
        [
            lesu,
            t_selera,
            pusing,
            suhu_tinggi
        ]
    ]
    septicaemia = [
        0.0,
        [
            lesu,
            t_darah,
            suhu_tinggi,
            luka
        ]
    ]
    lumpuh = [
        0.0,
        [
            lesu,
            t_bergerak
        ]
    ]
    mencret_berdarah = [
        0.0,
        [
            bab2,
            encer,
            darah,
            lesu,
            t_selera
        ]
    ]
    makan_daging = [
        0.0,
        [
            makan,
            daging
        ]
    ]
    makan_jamur = [
        0.0,
        [
            makan,
            jamur
        ]
    ]
    makan_kaleng = [
        0.0,
        [
            makan,
            kaleng
        ]
    ]
    minum_susu = [
        0.0,
        [
            b_susu,
            m_susu
        ]
    ]

    gejala = [mencret, muntah, s_perut, darah_rendah, koma, demam, septicaemia, lumpuh, mencret_berdarah, makan_daging, makan_jamur, makan_kaleng, minum_susu]
    # print(gejala)

    for gjala in gejala:
        n = 0
        m = len(gjala[1])
        for i in range(0, m):
            if gjala[1][i] != 't':
                n += 1
        gjala[0] = n/m

    # print(gejala)

    staphylococcus = [
        0,
        [
            mencret,
            muntah,
            s_perut,
            darah_rendah,
            makan_daging
        ]
    ]
    jamur_beracun = [
        0,
        [
            mencret,
            muntah,
            s_perut,
            koma,
            makan_jamur
        ]
    ]
    salmonallae = [
        0,
        [
            mencret,
            muntah,
            s_perut,
            demam,
            septicaemia,
            makan_daging
        ]
    ]
    clostridium = [
        0,
        [
            muntah,
            lumpuh,
            makan_kaleng
        ]
    ]
    campylobacter = [
        0,
        [
            mencret_berdarah,
            mencret,
            s_perut,
            demam,
            minum_susu
        ]
    ]

    penyakit = [staphylococcus, jamur_beracun, salmonallae, clostridium, campylobacter]

    for pnyakit in penyakit:
        n = 0
        m = len(pnyakit[1])
        for i in range(0, m):
            n += pnyakit[1][i][0]
        pnyakit[0] = (n/m) * 100

    thres = float(input('Threshold\t:'))

    i = 0
    for pnyakit in penyakit:
        if i == 0:
            nama = 'Staphylococcus'
        elif i == 1:
            nama = 'Jamur Beracun'
        elif i == 2:
            nama = 'Salmonellae'
        elif i == 3:
            nama = 'Clostridium '
        else:
            nama = 'Campylobacter'
        if pnyakit[0] > thres:
            namaTampil = nama
            thres = pnyakit[0]
        print(nama + '\t: ' + str(pnyakit[0]) + '%')
        i += 1
    print('Anda Terkena Infeksi '+ namaTampil)
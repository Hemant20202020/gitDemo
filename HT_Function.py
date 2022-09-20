def FACT(N):
    if N == 0 or N == 1:
        PFACT = 1
        return PFACT
    else:
        PFACT = 1
        for I in range(1, N + 1):
            PFACT = I * PFACT
    return PFACT


def HT(AL, LP, LQ, LR, LS, NO):
    LPR = LP + LR + 1
    LQS = LQ + LS + 1
    G2 = FACT(LQ)
    G3 = FACT(LR)
    G4 = FACT(LS)
    G5 = FACT(LPR)
    G6 = FACT(LQS)
    SUM = 1.0
    for I in range(1, NO + 1):
        LPO = LP + I
        G1 = FACT(LPO)
        G = (G1 * G2 * G3 * G4) / (G5 * G6)
        C1 = (3 ** I) * (AL ** I)
        PFACT = FACT(I)
        SUM = SUM + (C1 / PFACT) * G

    H = SUM

    return float(H)
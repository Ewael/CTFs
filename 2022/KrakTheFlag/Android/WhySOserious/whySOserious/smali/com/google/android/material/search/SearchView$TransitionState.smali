.class public final enum Lcom/google/android/material/search/SearchView$TransitionState;
.super Ljava/lang/Enum;
.source "SearchView.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/google/android/material/search/SearchView;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x4019
    name = "TransitionState"
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Ljava/lang/Enum<",
        "Lcom/google/android/material/search/SearchView$TransitionState;",
        ">;"
    }
.end annotation


# static fields
.field private static final synthetic $VALUES:[Lcom/google/android/material/search/SearchView$TransitionState;

.field public static final enum HIDDEN:Lcom/google/android/material/search/SearchView$TransitionState;

.field public static final enum HIDING:Lcom/google/android/material/search/SearchView$TransitionState;

.field public static final enum SHOWING:Lcom/google/android/material/search/SearchView$TransitionState;

.field public static final enum SHOWN:Lcom/google/android/material/search/SearchView$TransitionState;


# direct methods
.method static constructor <clinit>()V
    .locals 9

    .line 917
    new-instance v0, Lcom/google/android/material/search/SearchView$TransitionState;

    const-string v1, "HIDING"

    const/4 v2, 0x0

    invoke-direct {v0, v1, v2}, Lcom/google/android/material/search/SearchView$TransitionState;-><init>(Ljava/lang/String;I)V

    sput-object v0, Lcom/google/android/material/search/SearchView$TransitionState;->HIDING:Lcom/google/android/material/search/SearchView$TransitionState;

    .line 918
    new-instance v1, Lcom/google/android/material/search/SearchView$TransitionState;

    const-string v3, "HIDDEN"

    const/4 v4, 0x1

    invoke-direct {v1, v3, v4}, Lcom/google/android/material/search/SearchView$TransitionState;-><init>(Ljava/lang/String;I)V

    sput-object v1, Lcom/google/android/material/search/SearchView$TransitionState;->HIDDEN:Lcom/google/android/material/search/SearchView$TransitionState;

    .line 919
    new-instance v3, Lcom/google/android/material/search/SearchView$TransitionState;

    const-string v5, "SHOWING"

    const/4 v6, 0x2

    invoke-direct {v3, v5, v6}, Lcom/google/android/material/search/SearchView$TransitionState;-><init>(Ljava/lang/String;I)V

    sput-object v3, Lcom/google/android/material/search/SearchView$TransitionState;->SHOWING:Lcom/google/android/material/search/SearchView$TransitionState;

    .line 920
    new-instance v5, Lcom/google/android/material/search/SearchView$TransitionState;

    const-string v7, "SHOWN"

    const/4 v8, 0x3

    invoke-direct {v5, v7, v8}, Lcom/google/android/material/search/SearchView$TransitionState;-><init>(Ljava/lang/String;I)V

    sput-object v5, Lcom/google/android/material/search/SearchView$TransitionState;->SHOWN:Lcom/google/android/material/search/SearchView$TransitionState;

    .line 916
    const/4 v7, 0x4

    new-array v7, v7, [Lcom/google/android/material/search/SearchView$TransitionState;

    aput-object v0, v7, v2

    aput-object v1, v7, v4

    aput-object v3, v7, v6

    aput-object v5, v7, v8

    sput-object v7, Lcom/google/android/material/search/SearchView$TransitionState;->$VALUES:[Lcom/google/android/material/search/SearchView$TransitionState;

    return-void
.end method

.method private constructor <init>(Ljava/lang/String;I)V
    .locals 0
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()V"
        }
    .end annotation

    .line 916
    invoke-direct {p0, p1, p2}, Ljava/lang/Enum;-><init>(Ljava/lang/String;I)V

    return-void
.end method

.method public static valueOf(Ljava/lang/String;)Lcom/google/android/material/search/SearchView$TransitionState;
    .locals 1
    .param p0, "name"    # Ljava/lang/String;

    .line 916
    const-class v0, Lcom/google/android/material/search/SearchView$TransitionState;

    invoke-static {v0, p0}, Ljava/lang/Enum;->valueOf(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Enum;

    move-result-object v0

    check-cast v0, Lcom/google/android/material/search/SearchView$TransitionState;

    return-object v0
.end method

.method public static values()[Lcom/google/android/material/search/SearchView$TransitionState;
    .locals 1

    .line 916
    sget-object v0, Lcom/google/android/material/search/SearchView$TransitionState;->$VALUES:[Lcom/google/android/material/search/SearchView$TransitionState;

    invoke-virtual {v0}, [Lcom/google/android/material/search/SearchView$TransitionState;->clone()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, [Lcom/google/android/material/search/SearchView$TransitionState;

    return-object v0
.end method

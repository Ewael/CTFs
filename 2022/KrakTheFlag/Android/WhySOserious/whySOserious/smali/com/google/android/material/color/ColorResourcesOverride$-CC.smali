.class public final synthetic Lcom/google/android/material/color/ColorResourcesOverride$-CC;
.super Ljava/lang/Object;
.source "ColorResourcesOverride.java"


# annotations
.annotation build Lcom/android/tools/r8/annotations/SynthesizedClassV2;
    kind = 0x8
    versionHash = "ea87655719898b9807d7a88878e9de051d12af172d2fab563c9881b5e404e7d4"
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Ljava/lang/Object;"
    }
.end annotation


# direct methods
.method public static getInstance()Lcom/google/android/material/color/ColorResourcesOverride;
    .locals 2

    .line 44
    const/16 v0, 0x1e

    sget v1, Landroid/os/Build$VERSION;->SDK_INT:I

    if-gt v0, v1, :cond_0

    sget v0, Landroid/os/Build$VERSION;->SDK_INT:I

    const/16 v1, 0x21

    if-gt v0, v1, :cond_0

    .line 45
    invoke-static {}, Lcom/google/android/material/color/ResourcesLoaderColorResourcesOverride;->getInstance()Lcom/google/android/material/color/ColorResourcesOverride;

    move-result-object v0

    return-object v0

    .line 46
    :cond_0
    invoke-static {}, Landroidx/core/os/BuildCompat;->isAtLeastU()Z

    move-result v0

    if-eqz v0, :cond_1

    .line 49
    invoke-static {}, Lcom/google/android/material/color/ResourcesLoaderColorResourcesOverride;->getInstance()Lcom/google/android/material/color/ColorResourcesOverride;

    move-result-object v0

    return-object v0

    .line 51
    :cond_1
    const/4 v0, 0x0

    return-object v0
.end method

.class public final synthetic Landroidx/core/internal/view/SupportMenuItem$-CC;
.super Ljava/lang/Object;
.source "SupportMenuItem.java"


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
.method public static bridge synthetic $default$setContentDescription(Landroidx/core/internal/view/SupportMenuItem;Ljava/lang/CharSequence;)Landroid/view/MenuItem;
    .locals 0
    .param p0, "_this"    # Landroidx/core/internal/view/SupportMenuItem;

    .line 41
    invoke-interface {p0, p1}, Landroidx/core/internal/view/SupportMenuItem;->setContentDescription(Ljava/lang/CharSequence;)Landroidx/core/internal/view/SupportMenuItem;

    move-result-object p1

    return-object p1
.end method

.method public static bridge synthetic $default$setTooltipText(Landroidx/core/internal/view/SupportMenuItem;Ljava/lang/CharSequence;)Landroid/view/MenuItem;
    .locals 0
    .param p0, "_this"    # Landroidx/core/internal/view/SupportMenuItem;

    .line 41
    invoke-interface {p0, p1}, Landroidx/core/internal/view/SupportMenuItem;->setTooltipText(Ljava/lang/CharSequence;)Landroidx/core/internal/view/SupportMenuItem;

    move-result-object p1

    return-object p1
.end method

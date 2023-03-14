.class Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;
.super Landroid/widget/ArrayAdapter;
.source "MaterialAutoCompleteTextView.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "MaterialArrayAdapter"
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "<T:",
        "Ljava/lang/Object;",
        ">",
        "Landroid/widget/ArrayAdapter<",
        "Ljava/lang/String;",
        ">;"
    }
.end annotation


# instance fields
.field private pressedRippleColor:Landroid/content/res/ColorStateList;

.field private selectedItemRippleOverlaidColor:Landroid/content/res/ColorStateList;

.field final synthetic this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;


# direct methods
.method constructor <init>(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;Landroid/content/Context;I[Ljava/lang/String;)V
    .locals 0
    .param p2, "context"    # Landroid/content/Context;
    .param p3, "resource"    # I
    .param p4, "objects"    # [Ljava/lang/String;

    .line 423
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    iput-object p1, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    .line 424
    invoke-direct {p0, p2, p3, p4}, Landroid/widget/ArrayAdapter;-><init>(Landroid/content/Context;I[Ljava/lang/Object;)V

    .line 425
    invoke-virtual {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->updateSelectedItemColorStateList()V

    .line 426
    return-void
.end method

.method private createItemSelectedColorStateList()Landroid/content/res/ColorStateList;
    .locals 10

    .line 472
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    invoke-direct {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->hasSelectedColor()Z

    move-result v0

    if-eqz v0, :cond_0

    .line 473
    invoke-direct {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->hasSelectedRippleColor()Z

    move-result v0

    if-eqz v0, :cond_0

    .line 477
    const/4 v0, 0x2

    new-array v1, v0, [I

    fill-array-data v1, :array_0

    .line 478
    .local v1, "stateHovered":[I
    new-array v2, v0, [I

    fill-array-data v2, :array_1

    .line 480
    .local v2, "stateSelected":[I
    iget-object v3, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    .line 481
    invoke-static {v3}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$300(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)Landroid/content/res/ColorStateList;

    move-result-object v3

    const/4 v4, 0x0

    invoke-virtual {v3, v2, v4}, Landroid/content/res/ColorStateList;->getColorForState([II)I

    move-result v3

    .line 482
    .local v3, "colorSelected":I
    iget-object v5, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    .line 483
    invoke-static {v5}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$300(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)Landroid/content/res/ColorStateList;

    move-result-object v5

    invoke-virtual {v5, v1, v4}, Landroid/content/res/ColorStateList;->getColorForState([II)I

    move-result v5

    .line 485
    .local v5, "colorHovered":I
    const/4 v6, 0x3

    new-array v7, v6, [I

    iget-object v8, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    .line 487
    invoke-static {v8}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$200(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)I

    move-result v8

    invoke-static {v8, v3}, Lcom/google/android/material/color/MaterialColors;->layer(II)I

    move-result v8

    aput v8, v7, v4

    iget-object v8, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    .line 488
    invoke-static {v8}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$200(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)I

    move-result v8

    invoke-static {v8, v5}, Lcom/google/android/material/color/MaterialColors;->layer(II)I

    move-result v8

    const/4 v9, 0x1

    aput v8, v7, v9

    iget-object v8, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    .line 489
    invoke-static {v8}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$200(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)I

    move-result v8

    aput v8, v7, v0

    .line 491
    .local v7, "colors":[I
    new-array v6, v6, [[I

    aput-object v2, v6, v4

    aput-object v1, v6, v9

    new-array v4, v4, [I

    aput-object v4, v6, v0

    move-object v0, v6

    .line 493
    .local v0, "states":[[I
    new-instance v4, Landroid/content/res/ColorStateList;

    invoke-direct {v4, v0, v7}, Landroid/content/res/ColorStateList;-><init>([[I[I)V

    return-object v4

    .line 475
    .end local v0    # "states":[[I
    .end local v1    # "stateHovered":[I
    .end local v2    # "stateSelected":[I
    .end local v3    # "colorSelected":I
    .end local v5    # "colorHovered":I
    .end local v7    # "colors":[I
    :cond_0
    const/4 v0, 0x0

    return-object v0

    nop

    :array_0
    .array-data 4
        0x1010367
        -0x10100a7
    .end array-data

    :array_1
    .array-data 4
        0x10100a1
        -0x10100a7
    .end array-data
.end method

.method private getSelectedItemDrawable()Landroid/graphics/drawable/Drawable;
    .locals 4

    .line 448
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    invoke-direct {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->hasSelectedColor()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_1

    .line 456
    new-instance v0, Landroid/graphics/drawable/ColorDrawable;

    iget-object v2, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    invoke-static {v2}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$200(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)I

    move-result v2

    invoke-direct {v0, v2}, Landroid/graphics/drawable/ColorDrawable;-><init>(I)V

    .line 457
    .local v0, "colorDrawable":Landroid/graphics/drawable/Drawable;
    iget-object v2, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->pressedRippleColor:Landroid/content/res/ColorStateList;

    if-eqz v2, :cond_0

    .line 463
    iget-object v2, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->selectedItemRippleOverlaidColor:Landroid/content/res/ColorStateList;

    invoke-static {v0, v2}, Landroidx/core/graphics/drawable/DrawableCompat;->setTintList(Landroid/graphics/drawable/Drawable;Landroid/content/res/ColorStateList;)V

    .line 464
    new-instance v2, Landroid/graphics/drawable/RippleDrawable;

    iget-object v3, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->pressedRippleColor:Landroid/content/res/ColorStateList;

    invoke-direct {v2, v3, v0, v1}, Landroid/graphics/drawable/RippleDrawable;-><init>(Landroid/content/res/ColorStateList;Landroid/graphics/drawable/Drawable;Landroid/graphics/drawable/Drawable;)V

    return-object v2

    .line 466
    :cond_0
    return-object v0

    .line 449
    .end local v0    # "colorDrawable":Landroid/graphics/drawable/Drawable;
    :cond_1
    return-object v1
.end method

.method private hasSelectedColor()Z
    .locals 1

    .line 514
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    iget-object v0, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    invoke-static {v0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$200(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)I

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    return v0
.end method

.method private hasSelectedRippleColor()Z
    .locals 1

    .line 518
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    iget-object v0, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    invoke-static {v0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$300(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)Landroid/content/res/ColorStateList;

    move-result-object v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    return v0
.end method

.method private sanitizeDropdownItemSelectedRippleColor()Landroid/content/res/ColorStateList;
    .locals 6

    .line 497
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    invoke-direct {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->hasSelectedRippleColor()Z

    move-result v0

    if-nez v0, :cond_0

    .line 498
    const/4 v0, 0x0

    return-object v0

    .line 503
    :cond_0
    const/4 v0, 0x1

    new-array v1, v0, [I

    const v2, 0x10100a7

    const/4 v3, 0x0

    aput v2, v1, v3

    .line 504
    .local v1, "statePressed":[I
    const/4 v2, 0x2

    new-array v4, v2, [I

    iget-object v5, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    .line 506
    invoke-static {v5}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->access$300(Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;)Landroid/content/res/ColorStateList;

    move-result-object v5

    invoke-virtual {v5, v1, v3}, Landroid/content/res/ColorStateList;->getColorForState([II)I

    move-result v5

    aput v5, v4, v3

    aput v3, v4, v0

    .line 509
    .local v4, "colors":[I
    new-array v2, v2, [[I

    aput-object v1, v2, v3

    new-array v3, v3, [I

    aput-object v3, v2, v0

    move-object v0, v2

    .line 510
    .local v0, "states":[[I
    new-instance v2, Landroid/content/res/ColorStateList;

    invoke-direct {v2, v0, v4}, Landroid/content/res/ColorStateList;-><init>([[I[I)V

    return-object v2
.end method


# virtual methods
.method public getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;
    .locals 4
    .param p1, "position"    # I
    .param p2, "convertView"    # Landroid/view/View;
    .param p3, "parent"    # Landroid/view/ViewGroup;

    .line 435
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    invoke-super {p0, p1, p2, p3}, Landroid/widget/ArrayAdapter;->getView(ILandroid/view/View;Landroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    .line 437
    .local v0, "view":Landroid/view/View;
    instance-of v1, v0, Landroid/widget/TextView;

    if-eqz v1, :cond_1

    .line 438
    move-object v1, v0

    check-cast v1, Landroid/widget/TextView;

    .line 439
    .local v1, "textView":Landroid/widget/TextView;
    iget-object v2, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->this$0:Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;

    invoke-virtual {v2}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView;->getText()Landroid/text/Editable;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1}, Landroid/widget/TextView;->getText()Ljava/lang/CharSequence;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/String;->contentEquals(Ljava/lang/CharSequence;)Z

    move-result v2

    .line 440
    .local v2, "isSelectedItem":Z
    if-eqz v2, :cond_0

    invoke-direct {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->getSelectedItemDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v3

    goto :goto_0

    :cond_0
    const/4 v3, 0x0

    :goto_0
    invoke-static {v1, v3}, Landroidx/core/view/ViewCompat;->setBackground(Landroid/view/View;Landroid/graphics/drawable/Drawable;)V

    .line 443
    .end local v1    # "textView":Landroid/widget/TextView;
    .end local v2    # "isSelectedItem":Z
    :cond_1
    return-object v0
.end method

.method updateSelectedItemColorStateList()V
    .locals 1

    .line 429
    .local p0, "this":Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;, "Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter<TT;>;"
    invoke-direct {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->sanitizeDropdownItemSelectedRippleColor()Landroid/content/res/ColorStateList;

    move-result-object v0

    iput-object v0, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->pressedRippleColor:Landroid/content/res/ColorStateList;

    .line 430
    invoke-direct {p0}, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->createItemSelectedColorStateList()Landroid/content/res/ColorStateList;

    move-result-object v0

    iput-object v0, p0, Lcom/google/android/material/textfield/MaterialAutoCompleteTextView$MaterialArrayAdapter;->selectedItemRippleOverlaidColor:Landroid/content/res/ColorStateList;

    .line 431
    return-void
.end method

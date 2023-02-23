.class public abstract Landroid/support/v4/media/session/MediaSessionCompat$Callback;
.super Ljava/lang/Object;
.source "MediaSessionCompat.java"


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Landroid/support/v4/media/session/MediaSessionCompat;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x409
    name = "Callback"
.end annotation

.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi24;,
        Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi23;,
        Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi21;,
        Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;
    }
.end annotation


# instance fields
.field private mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

.field final mCallbackObj:Ljava/lang/Object;

.field private mMediaPlayPauseKeyPending:Z

.field mSessionImpl:Ljava/lang/ref/WeakReference;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/lang/ref/WeakReference<",
            "Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor <init>()V
    .locals 2

    .line 977
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 974
    const/4 v0, 0x0

    iput-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    .line 978
    sget v0, Landroid/os/Build$VERSION;->SDK_INT:I

    const/16 v1, 0x18

    if-lt v0, v1, :cond_0

    .line 979
    new-instance v0, Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi24;

    invoke-direct {v0, p0}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi24;-><init>(Landroid/support/v4/media/session/MediaSessionCompat$Callback;)V

    invoke-static {v0}, Landroid/support/v4/media/session/MediaSessionCompatApi24;->createCallback(Landroid/support/v4/media/session/MediaSessionCompatApi24$Callback;)Ljava/lang/Object;

    move-result-object v0

    iput-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackObj:Ljava/lang/Object;

    goto :goto_0

    .line 980
    :cond_0
    sget v0, Landroid/os/Build$VERSION;->SDK_INT:I

    const/16 v1, 0x17

    if-lt v0, v1, :cond_1

    .line 981
    new-instance v0, Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi23;

    invoke-direct {v0, p0}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi23;-><init>(Landroid/support/v4/media/session/MediaSessionCompat$Callback;)V

    invoke-static {v0}, Landroid/support/v4/media/session/MediaSessionCompatApi23;->createCallback(Landroid/support/v4/media/session/MediaSessionCompatApi23$Callback;)Ljava/lang/Object;

    move-result-object v0

    iput-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackObj:Ljava/lang/Object;

    goto :goto_0

    .line 982
    :cond_1
    nop

    .line 983
    new-instance v0, Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi21;

    invoke-direct {v0, p0}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$StubApi21;-><init>(Landroid/support/v4/media/session/MediaSessionCompat$Callback;)V

    invoke-static {v0}, Landroid/support/v4/media/session/MediaSessionCompatApi21;->createCallback(Landroid/support/v4/media/session/MediaSessionCompatApi21$Callback;)Ljava/lang/Object;

    move-result-object v0

    iput-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackObj:Ljava/lang/Object;

    .line 987
    :goto_0
    return-void
.end method


# virtual methods
.method handleMediaPlayPauseKeySingleTapIfPending(Landroidx/media/MediaSessionManager$RemoteUserInfo;)V
    .locals 13
    .param p1, "remoteUserInfo"    # Landroidx/media/MediaSessionManager$RemoteUserInfo;

    .line 1072
    iget-boolean v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mMediaPlayPauseKeyPending:Z

    if-nez v0, :cond_0

    .line 1073
    return-void

    .line 1075
    :cond_0
    const/4 v0, 0x0

    iput-boolean v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mMediaPlayPauseKeyPending:Z

    .line 1076
    iget-object v1, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;->removeMessages(I)V

    .line 1078
    iget-object v1, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mSessionImpl:Ljava/lang/ref/WeakReference;

    invoke-virtual {v1}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;

    .line 1079
    .local v1, "impl":Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;
    if-nez v1, :cond_1

    .line 1080
    return-void

    .line 1082
    :cond_1
    invoke-interface {v1}, Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;->getPlaybackState()Landroid/support/v4/media/session/PlaybackStateCompat;

    move-result-object v3

    .line 1083
    .local v3, "state":Landroid/support/v4/media/session/PlaybackStateCompat;
    const-wide/16 v4, 0x0

    if-nez v3, :cond_2

    move-wide v6, v4

    goto :goto_0

    :cond_2
    invoke-virtual {v3}, Landroid/support/v4/media/session/PlaybackStateCompat;->getActions()J

    move-result-wide v6

    .line 1084
    .local v6, "validActions":J
    :goto_0
    if-eqz v3, :cond_3

    .line 1085
    invoke-virtual {v3}, Landroid/support/v4/media/session/PlaybackStateCompat;->getState()I

    move-result v8

    const/4 v9, 0x3

    if-ne v8, v9, :cond_3

    const/4 v8, 0x1

    goto :goto_1

    :cond_3
    const/4 v8, 0x0

    .line 1086
    .local v8, "isPlaying":Z
    :goto_1
    const-wide/16 v9, 0x204

    and-long/2addr v9, v6

    cmp-long v11, v9, v4

    if-eqz v11, :cond_4

    const/4 v9, 0x1

    goto :goto_2

    :cond_4
    const/4 v9, 0x0

    .line 1088
    .local v9, "canPlay":Z
    :goto_2
    const-wide/16 v10, 0x202

    and-long/2addr v10, v6

    cmp-long v12, v10, v4

    if-eqz v12, :cond_5

    const/4 v0, 0x1

    .line 1090
    .local v0, "canPause":Z
    :cond_5
    invoke-interface {v1, p1}, Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;->setCurrentControllerInfo(Landroidx/media/MediaSessionManager$RemoteUserInfo;)V

    .line 1091
    if-eqz v8, :cond_6

    if-eqz v0, :cond_6

    .line 1092
    invoke-virtual {p0}, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->onPause()V

    goto :goto_3

    .line 1093
    :cond_6
    if-nez v8, :cond_7

    if-eqz v9, :cond_7

    .line 1094
    invoke-virtual {p0}, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->onPlay()V

    .line 1096
    :cond_7
    :goto_3
    const/4 v2, 0x0

    invoke-interface {v1, v2}, Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;->setCurrentControllerInfo(Landroidx/media/MediaSessionManager$RemoteUserInfo;)V

    .line 1097
    return-void
.end method

.method public onAddQueueItem(Landroid/support/v4/media/MediaDescriptionCompat;)V
    .locals 0
    .param p1, "description"    # Landroid/support/v4/media/MediaDescriptionCompat;

    .line 1291
    return-void
.end method

.method public onAddQueueItem(Landroid/support/v4/media/MediaDescriptionCompat;I)V
    .locals 0
    .param p1, "description"    # Landroid/support/v4/media/MediaDescriptionCompat;
    .param p2, "index"    # I

    .line 1303
    return-void
.end method

.method public onCommand(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/ResultReceiver;)V
    .locals 0
    .param p1, "command"    # Ljava/lang/String;
    .param p2, "extras"    # Landroid/os/Bundle;
    .param p3, "cb"    # Landroid/os/ResultReceiver;

    .line 1007
    return-void
.end method

.method public onCustomAction(Ljava/lang/String;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "action"    # Ljava/lang/String;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1281
    return-void
.end method

.method public onFastForward()V
    .locals 0

    .line 1189
    return-void
.end method

.method public onMediaButtonEvent(Landroid/content/Intent;)Z
    .locals 13
    .param p1, "mediaButtonEvent"    # Landroid/content/Intent;

    .line 1021
    sget v0, Landroid/os/Build$VERSION;->SDK_INT:I

    const/16 v1, 0x1b

    const/4 v2, 0x0

    if-lt v0, v1, :cond_0

    .line 1026
    return v2

    .line 1028
    :cond_0
    iget-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mSessionImpl:Ljava/lang/ref/WeakReference;

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;

    .line 1029
    .local v0, "impl":Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;
    if-eqz v0, :cond_8

    iget-object v1, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    if-nez v1, :cond_1

    goto :goto_3

    .line 1032
    :cond_1
    const-string v1, "android.intent.extra.KEY_EVENT"

    invoke-virtual {p1, v1}, Landroid/content/Intent;->getParcelableExtra(Ljava/lang/String;)Landroid/os/Parcelable;

    move-result-object v1

    check-cast v1, Landroid/view/KeyEvent;

    .line 1033
    .local v1, "keyEvent":Landroid/view/KeyEvent;
    if-eqz v1, :cond_7

    invoke-virtual {v1}, Landroid/view/KeyEvent;->getAction()I

    move-result v3

    if-eqz v3, :cond_2

    goto :goto_2

    .line 1036
    :cond_2
    invoke-interface {v0}, Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;->getCurrentControllerInfo()Landroidx/media/MediaSessionManager$RemoteUserInfo;

    move-result-object v3

    .line 1037
    .local v3, "remoteUserInfo":Landroidx/media/MediaSessionManager$RemoteUserInfo;
    invoke-virtual {v1}, Landroid/view/KeyEvent;->getKeyCode()I

    move-result v4

    .line 1038
    .local v4, "keyCode":I
    sparse-switch v4, :sswitch_data_0

    .line 1065
    invoke-virtual {p0, v3}, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->handleMediaPlayPauseKeySingleTapIfPending(Landroidx/media/MediaSessionManager$RemoteUserInfo;)V

    .line 1068
    return v2

    .line 1041
    :sswitch_0
    invoke-virtual {v1}, Landroid/view/KeyEvent;->getRepeatCount()I

    move-result v5

    const/4 v6, 0x1

    if-lez v5, :cond_3

    .line 1043
    invoke-virtual {p0, v3}, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->handleMediaPlayPauseKeySingleTapIfPending(Landroidx/media/MediaSessionManager$RemoteUserInfo;)V

    goto :goto_1

    .line 1044
    :cond_3
    iget-boolean v5, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mMediaPlayPauseKeyPending:Z

    if-eqz v5, :cond_6

    .line 1045
    iget-object v5, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    invoke-virtual {v5, v6}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;->removeMessages(I)V

    .line 1047
    iput-boolean v2, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mMediaPlayPauseKeyPending:Z

    .line 1048
    invoke-interface {v0}, Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;->getPlaybackState()Landroid/support/v4/media/session/PlaybackStateCompat;

    move-result-object v2

    .line 1049
    .local v2, "state":Landroid/support/v4/media/session/PlaybackStateCompat;
    const-wide/16 v7, 0x0

    if-nez v2, :cond_4

    move-wide v9, v7

    goto :goto_0

    :cond_4
    invoke-virtual {v2}, Landroid/support/v4/media/session/PlaybackStateCompat;->getActions()J

    move-result-wide v9

    .line 1051
    .local v9, "validActions":J
    :goto_0
    const-wide/16 v11, 0x20

    and-long/2addr v11, v9

    cmp-long v5, v11, v7

    if-eqz v5, :cond_5

    .line 1052
    invoke-virtual {p0}, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->onSkipToNext()V

    .line 1054
    .end local v2    # "state":Landroid/support/v4/media/session/PlaybackStateCompat;
    .end local v9    # "validActions":J
    :cond_5
    goto :goto_1

    .line 1055
    :cond_6
    iput-boolean v6, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mMediaPlayPauseKeyPending:Z

    .line 1056
    iget-object v2, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    invoke-virtual {v2, v6, v3}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v5

    .line 1059
    invoke-static {}, Landroid/view/ViewConfiguration;->getDoubleTapTimeout()I

    move-result v7

    int-to-long v7, v7

    .line 1056
    invoke-virtual {v2, v5, v7, v8}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;->sendMessageDelayed(Landroid/os/Message;J)Z

    .line 1061
    :goto_1
    return v6

    .line 1034
    .end local v3    # "remoteUserInfo":Landroidx/media/MediaSessionManager$RemoteUserInfo;
    .end local v4    # "keyCode":I
    :cond_7
    :goto_2
    return v2

    .line 1030
    .end local v1    # "keyEvent":Landroid/view/KeyEvent;
    :cond_8
    :goto_3
    return v2

    nop

    :sswitch_data_0
    .sparse-switch
        0x4f -> :sswitch_0
        0x55 -> :sswitch_0
    .end sparse-switch
.end method

.method public onPause()V
    .locals 0

    .line 1171
    return-void
.end method

.method public onPlay()V
    .locals 0

    .line 1136
    return-void
.end method

.method public onPlayFromMediaId(Ljava/lang/String;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "mediaId"    # Ljava/lang/String;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1143
    return-void
.end method

.method public onPlayFromSearch(Ljava/lang/String;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "query"    # Ljava/lang/String;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1152
    return-void
.end method

.method public onPlayFromUri(Landroid/net/Uri;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "uri"    # Landroid/net/Uri;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1158
    return-void
.end method

.method public onPrepare()V
    .locals 0

    .line 1104
    return-void
.end method

.method public onPrepareFromMediaId(Ljava/lang/String;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "mediaId"    # Ljava/lang/String;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1112
    return-void
.end method

.method public onPrepareFromSearch(Ljava/lang/String;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "query"    # Ljava/lang/String;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1122
    return-void
.end method

.method public onPrepareFromUri(Landroid/net/Uri;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "uri"    # Landroid/net/Uri;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1130
    return-void
.end method

.method public onRemoveQueueItem(Landroid/support/v4/media/MediaDescriptionCompat;)V
    .locals 0
    .param p1, "description"    # Landroid/support/v4/media/MediaDescriptionCompat;

    .line 1314
    return-void
.end method

.method public onRemoveQueueItemAt(I)V
    .locals 0
    .param p1, "index"    # I
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    .line 1325
    return-void
.end method

.method public onRewind()V
    .locals 0

    .line 1195
    return-void
.end method

.method public onSeekTo(J)V
    .locals 0
    .param p1, "pos"    # J

    .line 1209
    return-void
.end method

.method public onSetCaptioningEnabled(Z)V
    .locals 0
    .param p1, "enabled"    # Z

    .line 1234
    return-void
.end method

.method public onSetRating(Landroid/support/v4/media/RatingCompat;)V
    .locals 0
    .param p1, "rating"    # Landroid/support/v4/media/RatingCompat;

    .line 1217
    return-void
.end method

.method public onSetRating(Landroid/support/v4/media/RatingCompat;Landroid/os/Bundle;)V
    .locals 0
    .param p1, "rating"    # Landroid/support/v4/media/RatingCompat;
    .param p2, "extras"    # Landroid/os/Bundle;

    .line 1226
    return-void
.end method

.method public onSetRepeatMode(I)V
    .locals 0
    .param p1, "repeatMode"    # I

    .line 1250
    return-void
.end method

.method public onSetShuffleMode(I)V
    .locals 0
    .param p1, "shuffleMode"    # I

    .line 1265
    return-void
.end method

.method public onSkipToNext()V
    .locals 0

    .line 1177
    return-void
.end method

.method public onSkipToPrevious()V
    .locals 0

    .line 1183
    return-void
.end method

.method public onSkipToQueueItem(J)V
    .locals 0
    .param p1, "id"    # J

    .line 1165
    return-void
.end method

.method public onStop()V
    .locals 0

    .line 1201
    return-void
.end method

.method setSessionImpl(Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;Landroid/os/Handler;)V
    .locals 2
    .param p1, "impl"    # Landroid/support/v4/media/session/MediaSessionCompat$MediaSessionImpl;
    .param p2, "handler"    # Landroid/os/Handler;

    .line 990
    new-instance v0, Ljava/lang/ref/WeakReference;

    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mSessionImpl:Ljava/lang/ref/WeakReference;

    .line 991
    iget-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    if-eqz v0, :cond_0

    .line 992
    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;->removeCallbacksAndMessages(Ljava/lang/Object;)V

    .line 994
    :cond_0
    new-instance v0, Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    invoke-virtual {p2}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, p0, v1}, Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;-><init>(Landroid/support/v4/media/session/MediaSessionCompat$Callback;Landroid/os/Looper;)V

    iput-object v0, p0, Landroid/support/v4/media/session/MediaSessionCompat$Callback;->mCallbackHandler:Landroid/support/v4/media/session/MediaSessionCompat$Callback$CallbackHandler;

    .line 995
    return-void
.end method

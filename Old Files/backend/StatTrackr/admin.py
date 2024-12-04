from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum
from .models import Club, Player, PlayerStats, ClubStats

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'total_players', 'win_percentage_display', 'goals_per_game_display')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    readonly_fields = ('created_at', 'updated_at')

    def total_players(self, obj):
        return obj.players.count()
    total_players.short_description = 'Squad Size'

    def win_percentage_display(self, obj):
        percentage = obj.get_win_percentage()  # This is already a float
        formatted_percentage = f"{percentage:.1f}%"  # Format as a string
        color = "green" if percentage > 50 else "red"
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            formatted_percentage
        )
    win_percentage_display.short_description = 'Win Rate'

    def goals_per_game_display(self, obj):
        return f'{obj.get_goals_per_game():.2f}'
    goals_per_game_display.short_description = 'Goals/Game'
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'position', 'goals_display', 'assists_display', 'appearances_display')
    list_filter = ('position', 'club')
    search_fields = ('name', 'club__name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-stats__goals',)

    fieldsets = (
        ('Player Information', {
            'fields': ('name', 'club', 'position')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def goals_display(self, obj):
        return format_html(
            '<b style="color: {};">{}</b>',
            'green' if obj.stats.goals > 10 else 'black',
            obj.stats.goals
        )
    goals_display.short_description = 'Goals'

    def assists_display(self, obj):
        return obj.stats.assists
    assists_display.short_description = 'Assists'

    def appearances_display(self, obj):
        return obj.stats.appearances
    appearances_display.short_description = 'Apps'

@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'goals', 'assists', 'appearances', 'shots_accuracy_display')
    list_filter = ('player__position', 'player__club')
    search_fields = ('player__name', 'player__club__name')
    readonly_fields = ('shots_accuracy_display',)

    fieldsets = (
        ('General Statistics', {
            'fields': (
                'player', 'goals', 'assists', 'appearances', 'minutes_played',
                'yellow_cards', 'red_cards', 'substitution_on', 'substitution_off'
            )
        }),
        ('Attack Statistics', {
            'fields': (
                'shots', 'shots_on_target', 'goals_from_header', 'goals_from_penalty',
                'goals_from_freekick', 'offsides', 'passes', 'crosses', 'corners_taken'
            )
        }),
        ('Defense Statistics', {
            'fields': (
                'interceptions', 'blocks', 'tackles', 'clearances', 'own_goals',
                'penalties_conceded', 'aerial_battles_won', 'aerial_battles_lost'
            )
        }),
        ('Goalkeeper Statistics', {
            'fields': (
                'clean_sheets', 'goals_conceded', 'saves', 'penalties_saved',
                'high_claims', 'sweeper_clearances', 'goal_kicks'
            ),
            'classes': ('collapse',)
        })
    )

    def shots_accuracy_display(self, obj):
        accuracy = obj.player.get_shots_accuracy()
        return format_html(
            '<span style="color: {};">{:.1f}%</span>',
            'green' if accuracy > 50 else 'orange' if accuracy > 30 else 'red',
            accuracy
        )
    shots_accuracy_display.short_description = 'Shot Accuracy'

@admin.register(ClubStats)
class ClubStatsAdmin(admin.ModelAdmin):
    list_display = ('club', 'wins', 'losses', 'goals', 'goals_conceded', 'clean_sheets')
    list_filter = ('club__location',)
    search_fields = ('club__name',)

    fieldsets = (
        ('Match Statistics', {
            'fields': (
                'club', 'wins', 'losses', 'goals', 'goals_conceded',
                'yellow_cards', 'red_cards'
            )
        }),
        ('Attack Statistics', {
            'fields': (
                'shots', 'shots_on_target', 'goals_from_header', 'goals_from_penalty',
                'goals_from_freekick', 'goals_from_inside_box', 'goals_from_outside_box',
                'offsides'
            )
        }),
        ('Defense Statistics', {
            'fields': (
                'clean_sheets', 'saves', 'blocks', 'interceptions', 'tackles',
                'clearances', 'own_goals', 'penalties_conceded', 'fouls'
            )
        })
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return ('club',) + self.readonly_fields
        return self.readonly_fields
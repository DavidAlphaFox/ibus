/* vim:set et sts=4: */
/* IBus - The Input Bus
 * Copyright (C) 2008-2009 Huang Peng <shawn.p.huang@gmail.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */
#ifndef __MATCH_RULE_H_
#define __MATCH_RULE_H_

#include <ibus.h>
#include "connection.h"

/*
 * Type macros.
 */

/* define GOBJECT macros */
#define BUS_TYPE_MATCH_RULE             \
    (bus_match_rule_get_type ())
#define BUS_MATCH_RULE(obj)             \
    (G_TYPE_CHECK_INSTANCE_CAST ((obj), BUS_TYPE_MATCH_RULE, BusMatchRule))
#define BUS_MATCH_RULE_CLASS(klass)     \
    (G_TYPE_CHECK_CLASS_CAST ((klass), BUS_TYPE_MATCH_RULE, BusMatchRuleClass))
#define BUS_IS_MATCH_RULE(obj)          \
    (G_TYPE_CHECK_INSTANCE_TYPE ((obj), BUS_TYPE_MATCH_RULE))
#define BUS_IS_MATCH_RULE_CLASS(klass)  \
    (G_TYPE_CHECK_CLASS_TYPE ((klass), BUS_TYPE_MATCH_RULE))
#define BUS_MATCH_RULE_GET_CLASS(obj)   \
    (G_TYPE_CHECK_GET_CLASS ((obj), BUS_TYPE_MATCH_RULE, BusMatchRuleClass))

G_BEGIN_DECLS

typedef struct _BusMatchRule BusMatchRule;
typedef struct _BusMatchRuleClass BusMatchRuleClass;

typedef enum {
    MATCH_TYPE          = 1 << 0,
    MATCH_INTERFACE     = 1 << 1,
    MATCH_MEMBER        = 1 << 2,
    MATCH_SENDER        = 1 << 3,
    MATCH_DESTINATION   = 1 << 4,
    MATCH_PATH          = 1 << 5,
    MATCH_ARGS          = 1 << 6,
} BusMatchFlags;

typedef struct _BusRecipient BusRecipient;
struct _BusRecipient {
    BusConnection *connection;
    gint refcount;
};

struct _BusMatchRule {
    IBusProxy parent;
    /* instance members */
    gint   flags;
    gint   message_type;
    gchar *interface;
    gchar *member;
    gchar *sender;
    gchar *destination;
    gchar *path;
    GArray *args;
    GList  *recipients;
};

struct _BusMatchRuleClass {
    IBusProxyClass parent;
    /* class members */
};

GType            bus_match_rule_get_type    (void);
BusMatchRule    *bus_match_rule_new         (const gchar    *text);
BusMatchRule    *bus_match_rule_ref         (BusMatchRule   *rule);
void             bus_match_rule_unref       (BusMatchRule   *rule);
void             bus_match_rule_free        (BusMatchRule   *rule);
gboolean         bus_match_rule_set_message_type
                                            (BusMatchRule   *rule,
                                             gint            type);
gboolean         bus_match_rule_set_sender  (BusMatchRule   *rule,
                                             const gchar    *sender);
gboolean         bus_match_rule_set_interface
                                            (BusMatchRule   *rule,
                                             const gchar    *interface);
gboolean         bus_match_rule_set_member  (BusMatchRule   *rule,
                                             const gchar    *member);
gboolean         bus_match_rule_set_path    (BusMatchRule   *rule,
                                             const gchar    *path);
gboolean         bus_match_rule_set_destination
                                            (BusMatchRule   *rule,
                                             const gchar    *dest);
gboolean         bus_match_rule_set_arg     (BusMatchRule   *rule,
                                             guint           arg_i,
                                             const gchar    *arg);
gboolean         bus_match_rule_match       (BusMatchRule   *rule,
                                             DBusMessage    *message);
gboolean         bus_match_rule_is_equal    (BusMatchRule   *a,
                                             BusMatchRule   *b);
void             bus_match_rule_add_recipient
                                            (BusMatchRule   *rule,
                                             BusConnection  *connection);
void             bus_match_rule_remove_recipient
                                            (BusMatchRule   *rule,
                                             BusConnection  *connection);
gboolean         bus_match_rule_get_recipients
                                            (BusMatchRule   *rule,
                                             DBusMessage    *message,
                                             GList          **recipients);

G_END_DECLS
#endif

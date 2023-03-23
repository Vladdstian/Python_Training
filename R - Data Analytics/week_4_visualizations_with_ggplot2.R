library("ggplot2")
library("palmerpenguins")

# COMMON SEQUENCE for PLOTTING WITH GGPLOT2

ggplot(data = penguins)+ 
  geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g,shape = species, alpha = species), color="purple")
 
# plotting with ggplot starts with ggplot() function
# after the data we want plotted is passed as argument for that function
# plus sign ('+') is used to add layers to the plot
# in ggplot2, plots are build through combinations of layers
# we choose geom_point() function to represent our data through points and create a scatter plot
# mapping=aes() tells R what aesthetics to use for the plot
# we use aes to define the mapping between the data and the plot
# we map the data from flipper_length to the x-axis and body_mass_g to the y-axis
# example:   aes(name_of_aesthetic = name_of_the_variable)


# SCATERPLOTS
ggplot(data = penguins)+ 
  geom_smooth(mapping = aes(x = flipper_length_mm, y = body_mass_g), color="blue")+
  geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g,shape = species, alpha = species), color="purple")

ggplot(data = penguins)+ 
  geom_smooth(mapping = aes(x = flipper_length_mm, y = body_mass_g, linetype = species))

ggplot(data = penguins)+ 
  geom_jitter(mapping = aes(x = flipper_length_mm, y = body_mass_g))

# BARCHARTS
ggplot(data=diamonds)+
  geom_bar(mapping = aes(x=cut, fill=clarity))+
  facet_grid(~cut)

# FACET
ggplot(data = penguins)+ 
  geom_smooth(mapping = aes(x = flipper_length_mm, y = body_mass_g, color=species))+
  facet_wrap(~species)

# LABELS
ggplot(data = penguins)+ 
  geom_smooth(mapping = aes(x = flipper_length_mm, y = body_mass_g, color=species))+
  labs(title="PALMER Penguins: Body Mass vs. Flipper Length")


# ANNOTATIONS
ggplot(data = penguins)+ 
  geom_smooth(mapping = aes(x = flipper_length_mm, y = body_mass_g, color=species))+
  annotate("text", x=220, y=3500, label="The Gentoos are the largest")